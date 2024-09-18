import memory_buffer_doubling as memb
import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import csv

"""
Goal of this program: 
- computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- all chains have the same length but some have more repeater stations in between. This implies a shorter distance and therefore the generation probability is larger
"""

"""simulation parameters"""
#memory_numbers = [2,1,1,2,2,1,1,2]
#generation_probability=0.01
#swapping_probability = 0.5
number_of_repetitions_original=2000 
element_numbers = 4

length_vec = [100, 50, 25, 12.5]
afix = [8,4,2,1]

file_name_list = ["compare_fixed_length_32-2.csv", "compare_fixed_buffers_32-4.csv", "compare_fixed_buffers_32-8.csv", "compare_fixed_buffers_32-16.csv"] ### file names: compare_fixed_buffers_const-bfix_.csv

def prob_function(length):
    Latt = 22
    return np.exp(-length/Latt)   



dataa = np.linspace(0.1,1,46)

"""vary distribution of memory_numbers"""

for j in range(len(afix)):
    a = afix[j]
    memory_numbers = [a,a,a,a,a,a,a,a]
    file_name = file_name_list[j]
    #print(memory_numbers)
    gen_prob = prob_function(length_vec[j])
    print(gen_prob)
    
    number_of_repetitions = number_of_repetitions_original



    """varry swapping_probability"""
    for sw_prob in reversed(dataa):
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
            print("new number of repetitions: ", number_of_repetitions)
            data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)


        print("length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])              
        
        "Daten in csv schreiben"
        with open(file_name, mode='a') as csvfile:
            csvfile_writer = csv.writer(csvfile, delimiter=',')
            csvfile_writer.writerow([element_numbers, gen_prob, sw_prob, data[0], data[1], number_of_repetitions, a, data[1]/data[0]])




