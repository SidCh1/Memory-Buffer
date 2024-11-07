import diff_p_doubling as memb
import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

"""
Goal of this program: 
- computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- all chains have the same length but some have more repeater stations in between. This implies a shorter distance and therefore the generation probability is larger
"""

"""simulation parameters"""

max_len = 100
total_buffer = 32
number_of_repetitions_original= 10

# memory_numbers_list = [3,3,3,3,7,7,3,3] # distribution of memory buffers
# segment_lengths = [20,20,40,20] # distance of each segment

memory_numbers_list = [4,4,4,4,4,4,4,4] # distribution of memory buffers
segment_lengths = [20,20,40,20] # distance of each segment

num_segments = len(memory_numbers_list)/2 # number of segments

# chain_length_power = [1,2,3,4]

file_name_list = ["compare_fixed_length_32-4_dl.csv"] ### file names: compare_fixed_buffers_const-bfix_.csv

def gen_prob_function(length):
    Latt = 22
    return np.exp(-length/Latt)   

# gen_prob = gen_prob_function(max_len/ns)

generation_probability = [gen_prob_function(segment_lengths[0]), gen_prob_function(segment_lengths[1]), gen_prob_function(segment_lengths[2]), gen_prob_function(segment_lengths[3])]

dataa = np.linspace(0.1,1,10) # Swapping probability range


"""vary distribution of memory_numbers"""

for m in range(1):
    # a = int(total_buffer*(2**(-m-1))) # no of memories per station
    memory_numbers = memory_numbers_list# memory distribution list
    file_name = file_name_list[0] # file name to write into csv
    
    number_of_repetitions = number_of_repetitions_original
    generation_probability = generation_probability


    """vary swapping_probability"""
    for sw_prob in reversed(dataa):
        #print(i) 
        #swapping_probability=amin + i*stepsize
        #generation_probability =amin + i*stepsize
        #print(swapping_probability)
        data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=generation_probability,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)

        #print("length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])
        
        while (data[1]/data[0]) > 0.01:
            number_of_repetitions = 2*number_of_repetitions
            #print("new number of repetitions: ", number_of_repetitions)
            data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=generation_probability,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)


        #print("length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])              
        


        



        # "Daten in csv schreiben"
        # with open(file_name, mode='a') as csvfile:
        #     csvfile_writer = csv.writer(csvfile, delimiter=',')
        #     csvfile_writer.writerow([memory_numbers_list,num_segments, generation_probability, sw_prob, data[0], data[1], number_of_repetitions, data[1]/data[0]]) #data[0] is mean and [1] is error of AWT


        # Check if the file exists
        file_exists = os.path.exists(file_name)

        # Open the CSV file in append mode ('a')
        with open(file_name, mode='a', newline='') as csvfile:
            csvfile_writer = csv.writer(csvfile, delimiter=',')

            # If the file doesn't exist, write the header
            if not file_exists:
                csvfile_writer.writerow([
                    'memory_numbers_list', 'num_segments', 'generation_probability', 
                    'swapping_probability', 'AWT_mean', 'AWT_error', 'number_of_repetitions', 'AWT_ratio'
                ])

            # Write the data row
            csvfile_writer.writerow([
                memory_numbers_list, num_segments, generation_probability, sw_prob, 
                data[0], data[1], number_of_repetitions, data[1] / data[0]
            ])

