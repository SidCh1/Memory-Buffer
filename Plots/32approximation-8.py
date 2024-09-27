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
swapping_probability = 0.2
number_of_repetitions_original=2000 
element_numbers = 8


k = 2
memory_numbers = [k, k, k, k, k, k, k, k,k, k, k, k, k, k, k, k]


sw_prob_list = [0.2,0.4,0.5,0.7,1]


file_name_list = ["32approximation_8_2_a2_homo.csv",
"32approximation_8_2_a4.csv_homo",
"32approximation_8_2_a5.csv_homo",
"32approximation_8_2_a7.csv_homo",
"32approximation_8_2_a10.csv_homo"] ### file names: compare_fixed_buffers_const-bfix_.csv


#sw_prob = swapping_probability
datap = np.linspace(0.005,0.1,96)

"""vary distribution of memory_numbers"""

for j in range(len(sw_prob_list)):
    sw_prob = sw_prob_list[j]
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
            csvfile_writer.writerow([element_numbers, gen_prob, sw_prob, data[0], data[1], number_of_repetitions, k , data[1]/data[0]])




