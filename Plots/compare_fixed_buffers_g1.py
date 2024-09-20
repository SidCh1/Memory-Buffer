import memory_buffer_doubling as memb
import scipy.special
import numpy as np
import csv

"""
Goal of this program: 
- computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- make plots: waiting_time(swapping_probability) for different memory distributions
"""

"""simulation parameters"""
#memory_numbers = [2,1,1,2,2,1,1,2]
#generation_probability=0.01
swapping_probability = 0.1
number_of_repetitions_original=2000 
element_numbers = 4

const = 16
bfix = [15,14,13,12,11,10,9,8]
afix = [const - b for b in bfix]

file_name_list = ["compare_fixed_buffers_16-15_a1_pgros.csv", 
"compare_fixed_buffers_16-14_a1_pgros.csv",
"compare_fixed_buffers_16-13_a1_pgros.csv",
"compare_fixed_buffers_16-12_a1_pgros.csv",
"compare_fixed_buffers_16-11_a1_pgros.csv",
"compare_fixed_buffers_16-10_a1_pgros.csv",
"compare_fixed_buffers_16-9_a1_pgros.csv",
"compare_fixed_buffers_16-8_a1_pgros.csv",
"compare_fixed_buffers_16-7_a1_pgros.csv"] ### file names: compare_fixed_buffers_const-bfix_.csv


sw_prob = swapping_probability
datap = np.linspace(0.005,0.95,46)

"""vary distribution of memory_numbers"""

for j in range(len(bfix)):
    b = bfix[j]
    a = afix[j]
    memory_numbers = [b,a,a,b,b,a,a,b]
    file_name = file_name_list[j]
    #print(memory_numbers)
    
    number_of_repetitions = number_of_repetitions_original



    """varry swapping_probability"""
    for gen_prob in reversed(datap):
        #print(i) 
        #swapping_probability=amin + i*stepsize
        #generation_probability =amin + i*stepsize
        #print(swapping_probability)
        data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)

        #print("length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])
        
        while (data[1]/data[0]) > 0.01:
            number_of_repetitions = 2*number_of_repetitions
            #print("new number of repetitions: ", number_of_repetitions)
            data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)


        #print("length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])              
        
        "Daten in csv schreiben"
        with open(file_name, mode='a') as csvfile:
            csvfile_writer = csv.writer(csvfile, delimiter=',')
            csvfile_writer.writerow([element_numbers, gen_prob, sw_prob, data[0], data[1], number_of_repetitions, a, b, data[1]/data[0]])




