import memory_buffer_doubling as memb
import scipy.special
import numpy as np
#import matplotlib.pyplot as plt
import csv

"""
Goal of this program: 
- find saturation parameters for buffer distribution
"""

"""simulation parameters"""




#number_of_repetitions=500 

#datap = [0.1] # np.linspace(0.05,0.1,51)
#sw_prob_list = [0.5] #np.linspace(0.1,1,91)

file_name = "saturation_parameters_diff001_p005-01.csv"
element_numbers = 4


with open('Data/infty_buffer3_p005-01.csv','r') as csvfile:
    plots=csv.reader(csvfile, delimiter=',')
    #next(plots) #damit die erste zeile nicht eingelesen werden
    for row in plots:
        gen_prob = float(row[1])
        sw_prob = float(row[2])
        mean_inf = float(row[3])
        error_inf = float(row[4])
        number_of_repetitions = int(row[5]) 
        
        #print(gen_prob, sw_prob, mean_inf, error_inf, number_of_repetitions)
        
        #mean_previous = mean_inf
        #error_previous = error_inf 

    
        a = 1
        b = 10000
        memory_numbers = [b,a,a,b,b,a,a,b]


        data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)
        
        #print(memory_numbers, "length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])
                         
        
        
        while abs(data[0] - mean_inf) >  0.01*mean_inf:
            #print("Differenz vorher: ", abs(mean_previous - data[0]), error_previous)
            a += 1
            #print(a)
            memory_numbers = [b,a,a,b,b,a,a,b] 
            #print(memory_numbers)
            
            #mean_previous = data[0]
            #error_previous = data[1]
            
            data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)
            #print(memory_numbers, "length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])              
            #print("Differenz nachher: ", abs(mean_previous - data[0]), data[1])
            
            
            
        afix = a
        b = a
        memory_numbers = [b,a,a,b,b,a,a,b]
        
        data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)
                          
        #mean_previous = mean_inf
        #error_previous = error_inf                  
                          
        while abs(data[0] - mean_inf) >  0.01*mean_inf:
            #print("Differenz vorher: ", abs(mean_previous - data[0]), error_previous)
            b += 1
            #print(b)
            memory_numbers = [b,a,a,b,b,a,a,b] 
            #print(memory_numbers)
            
            #mean_previous = data[0]
            #error_previous = data[1]    
            
            data = memb.get_statistics(memory_numbers = memory_numbers,
                          generation_probability=gen_prob,
                          swapping_probability=sw_prob,
                          number_of_repetitions=number_of_repetitions)
            #print(memory_numbers, "length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])              
            #print("Differenz nachher: ", abs(mean_previous - data[0]), data[1])
            
                          
        
        #print(memory_numbers, "length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "AWT=", data[0], "+-", data[1])
        
        bfix = b    
        
        #print("fertig: ", mean_previous - data[0], error_previous)
        #print("final: ", memory_numbers, afix, bfix, "length=", element_numbers ,",generation_prob=", gen_prob,", swapping_prob=", sw_prob, "memory_buffer = 2, AWT=", data[0], "+-", data[1], ", ATW_inf=" , mean_inf, "+-", error_inf)
        "Daten in csv schreiben"
        with open(file_name, mode='a') as csvfile:
            csvfile_writer = csv.writer(csvfile, delimiter=',')
            csvfile_writer.writerow([element_numbers, gen_prob, sw_prob, data[0], data[1], number_of_repetitions, afix, bfix, mean_inf, error_inf, (data[0]-mean_inf)/mean_inf])

    






