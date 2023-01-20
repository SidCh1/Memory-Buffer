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
generation_probability=0.01
#swapping_probability=1
number_of_repetitions=100  

memory_numbers_list = [[1,1,1,1,1,1,1,1],[2,1,1,2,2,1,1,2],[3,1,1,1,1,1,1,3],[2,1,2,1,2,1,2,1]]

steps = 20
amin = 0.4
amax = 1
stepsize =  (amax-amin)/steps 

dataa = []
datamean_list = []
datastdev_list = []


dataa = [amin + i*stepsize for i in range(1,steps+1)]
#print(dataa)

"""vary distribution of memory_numbers"""

for j in range(len(memory_numbers_list)):
    memory_numbers = memory_numbers_list[j]
    #print(memory_numbers)
    datamean = []
    datastdev = []

    """varry swapping_probability"""
    for i in range(1,steps+1):
        #print(i) 
        swapping_probability=amin + i*stepsize
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

plt.xlabel('swapping probability $a$')
plt.ylabel(r'waiting time')
plt.title('generation probability=%f' %(generation_probability))


plt.legend()
plt.show()
