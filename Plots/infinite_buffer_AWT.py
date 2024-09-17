import memory_buffer_doubling as memb
import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import csv

"""
Goal of this program: 
- compute AWTs for infty buffer space number
"""

"""simulation parameters"""
const = 10000
memory_numbers = [const,const,const,const,const,const,const,const]
element_numbers = len(memory_numbers)/2

number_of_repetitions_original = 2000 

datap = np.linspace(0.005,0.015,51)
sw_prob_list = np.linspace(0.1,1,46)

file_name = "infty_buffer3_p005-01.csv"







"""vary distribution of memory_numbers"""

for sw_prob in sw_prob_list:

    number_of_repetitions = number_of_repetitions_original
    """varr generation_probability"""
    for gen_prob in reversed(datap):


        
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
            csvfile_writer.writerow([element_numbers, gen_prob, sw_prob, data[0], data[1], number_of_repetitions, data[1]/data[0]])

    






