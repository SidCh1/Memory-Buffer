import memory_buffer_doubling as memb
import scipy.special
import numpy as np
import matplotlib.pyplot as plt

"""
Goal of this program: 
- computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- make plots: waiting_time(swapping_probability) for different memory distributions
"""

"""simulation parameters"""
#memory_numbers = [1,1,1,1,1,1,1,1]
#generation_probability=0.01
swapping_probability=0.5
number_of_repetitions=1000  

const=1000
memory_numbers_list = [
    #[1,1,1,1,1,1,1,1],
    #[2,1,1,2,2,1,1,2],
    #[3,1,1,1,1,1,1,3],
    #[2,1,2,1,2,1,2,1],
    #[5,5,5,5,5,5,5,5],
    #[10,10,10,10,10,10,10,10],
    #[100,100,100,100,100,100,100,100]
    [const,1,1,const,const,1,1,const],
    [const,2,2,const,const,2,2,const],
    [const,3,3,const,const,3,3,const],
    [const,4,4,const,const,4,4,const],
    [const,5,5,const,const,5,5,const],
    #[const,6,6,const,const,6,6,const],
    #[const,7,7,const,const,7,7,const],
    #[const,8,8,const,const,8,8,const],
    ]

steps = 9
amin = 0.1
amax = 1
stepsize =  (amax-amin)/steps 

dataa = []
datamean_list = []
datastdev_list = []


dataa = [amin + i*stepsize for i in range(0,steps+1)]
#print(dataa)

"""vary distribution of memory_numbers"""

for j in range(len(memory_numbers_list)):
    memory_numbers = memory_numbers_list[j]
    #print(memory_numbers)
    datamean = []
    datastdev = []

    """varry swapping_probability"""
    for i in range(0,steps+1):
        #print(i) 
        #swapping_probability=amin + i*stepsize
        generation_probability =amin + i*stepsize
        #print(swapping_probability)
        data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=generation_probability,
                          swapping_probability=swapping_probability,
                          number_of_repetitions=number_of_repetitions)
        #print(data)
        #dataa.append(swapping_probability)
        datamean.append(data[0])
        datastdev.append(data[1])

    #print(datamean)
    datamean_list.append(datamean)
    datastdev_list.append(datastdev)

for j in range(len(memory_numbers_list)):
    plt.errorbar(dataa,datamean_list[j],datastdev_list[j],
             fmt ='x',capsize=3,label=r'%s' %(memory_numbers_list[j]))

#plt.xlabel('swapping probability $a$')
plt.xlabel('generation probability $p$')
plt.ylabel(r'waiting time')
#plt.title('generation probability=%f, number_of_repetitions=%i' %(generation_probability,number_of_repetitions))
plt.title('swapping probability=%f, number_of_repetitions=%i' %(swapping_probability,number_of_repetitions))


plt.legend()
plt.show()
