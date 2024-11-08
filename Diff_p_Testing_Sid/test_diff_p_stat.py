import diff_p_doubling as memb
import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

"""
Goal of this program: 
- Computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- Each segment has different lengths, so different generation probabilities.
- Total distance is fixed, and total memory buffer size is also fixed, but the number of segments can vary.
"""

"""simulation parameters"""

max_len = 100
total_buffer = 32
number_of_repetitions_original = 10

# Define the different configurations as a list of dictionaries
configurations = [
    {
        "memory_numbers_list": [3, 3, 3, 3, 7, 7, 3, 3],
        "segment_lengths": [40, 40, 80, 40],
        "file_name": "compare_fixed_length_32-4_a11_20_40_37_200km.csv",
    },
    {
        "memory_numbers_list": [7, 7, 3, 3, 3, 3, 3, 3],
        "segment_lengths": [40, 20, 20, 20],
        "file_name": "compare_fixed_length_32-4_40_20_73.csv",
    },
    {
        "memory_numbers_list": [3, 3, 3, 3, 7, 7, 3, 3],
        "segment_lengths": [15, 15, 55, 15],
        "file_name": "compare_fixed_length_32-4_15_55_37.csv",
    },
    {
        "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
        "segment_lengths": [20, 20, 40, 20],
        "file_name": "compare_fixed_length_32-4_a11_20_40.csv",
    },
    {
        "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
        "segment_lengths": [15, 15, 55, 15],
        "file_name": "compare_fixed_length_32-4_15_55.csv",
    },
    {
        "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
        "segment_lengths": [25, 25, 25, 25],
        "file_name": "compare_fixed_length_32-4_25_25.csv",
    },
]


def gen_prob_function(length):
    Latt = 44
    return np.exp(-length / Latt)


dataa = np.linspace(0.1, 1, 10)  # Swapping probability range

# Iterate over each configuration
for config in configurations:
    memory_numbers_list = config["memory_numbers_list"]
    segment_lengths = config["segment_lengths"]
    file_name = config["file_name"]

    num_segments = len(memory_numbers_list) / 2  # number of segments
    generation_probability = [gen_prob_function(length) for length in segment_lengths]

    """vary swapping_probability"""
    for sw_prob in reversed(dataa):
        data = memb.get_statistics(
            memory_numbers=memory_numbers_list,
            generation_probability=generation_probability,
            swapping_probability=sw_prob,
            number_of_repetitions=number_of_repetitions_original,
        )

        number_of_repetitions = number_of_repetitions_original
        while (data[1] / data[0]) > 0.01:
            number_of_repetitions *= 2
            data = memb.get_statistics(
                memory_numbers=memory_numbers_list,
                generation_probability=generation_probability,
                swapping_probability=sw_prob,
                number_of_repetitions=number_of_repetitions,
            )

        file_exists = os.path.exists(file_name)
        with open(file_name, mode="a", newline="") as csvfile:
            csvfile_writer = csv.writer(csvfile, delimiter=",")

            if not file_exists:
                csvfile_writer.writerow(
                    [
                        "memory_numbers_list",
                        "num_segments",
                        "segment_lengths",
                        "generation_probability",
                        "swapping_probability",
                        "AWT_mean",
                        "AWT_error",
                        "number_of_repetitions",
                        "AWT_ratio",
                    ]
                )

            csvfile_writer.writerow(
                [
                    memory_numbers_list,
                    num_segments,
                    segment_lengths,
                    generation_probability,
                    sw_prob,
                    data[0],
                    data[1],
                    number_of_repetitions,
                    data[1] / data[0],
                ]
            )


# import diff_p_doubling as memb
# import scipy.special
# import numpy as np
# import matplotlib.pyplot as plt
# import csv
# import os

# """
# Goal of this program:
# - computes waiting times for different swapping_probabilities and distributions of memory_numbers.
# - Each segment has different length so different generation probability.
# - Total distance is fixed and total memory buffer size is also fixed but number of segments can be varied.
# """

# """simulation parameters"""

# max_len = 200
# total_buffer = 32
# number_of_repetitions_original = 10

# memory_numbers_list = [3, 3, 3, 3, 7, 7, 3, 3]  # distribution of memory buffers
# segment_lengths = [40, 40, 80, 40]  # distance of each segment
# file_name_list = ["compare_fixed_length_32-4_a11_20_40_37_200km.csv"]

# # memory_numbers_list = [7,7,3,3,3,3,3,3] # distribution of memory buffers
# # segment_lengths = [40,20,20,20] # distance of each segment
# # file_name_list = ["compare_fixed_length_32-4_40_20_73.csv"]

# # memory_numbers_list = [3,3,3,3,7,7,3,3] # distribution of memory buffers
# # segment_lengths = [15,15,55,15] # distance of each segment
# # file_name_list = ["compare_fixed_length_32-4_15_55_37.csv"]

# # memory_numbers_list = [4,4,4,4,4,4,4,4] # distribution of memory buffers
# # segment_lengths = [20,20,40,20] # distance of each segment
# # file_name_list = ["compare_fixed_length_32-4_a11_20_40.csv"]

# # memory_numbers_list = [4,4,4,4,4,4,4,4] # distribution of memory buffers
# # segment_lengths = [15,15,55,15] # distance of each segment
# # file_name_list = ["compare_fixed_length_32-4_15_55.csv"]

# # memory_numbers_list = [4,4,4,4,4,4,4,4] # distribution of memory buffers
# # segment_lengths = [25,25,25,25] # distance of each segment
# # file_name_list = ["compare_fixed_length_32-4_25_25.csv"]

# num_segments = len(memory_numbers_list) / 2  # number of segments


# def gen_prob_function(length):
#     Latt = 11
#     return np.exp(-length / Latt)


# generation_probability = [
#     gen_prob_function(segment_lengths[0]),
#     gen_prob_function(segment_lengths[1]),
#     gen_prob_function(segment_lengths[2]),
#     gen_prob_function(segment_lengths[3]),
# ]

# dataa = np.linspace(0.1, 1, 10)  # Swapping probability range


# """vary distribution of memory_numbers"""

# for m in range(1):
#     # a = int(total_buffer*(2**(-m-1))) # no of memories per station
#     memory_numbers = memory_numbers_list  # memory distribution list
#     file_name = file_name_list[0]  # file name to write into csv

#     number_of_repetitions = number_of_repetitions_original
#     generation_probability = generation_probability

#     """vary swapping_probability"""
#     for sw_prob in reversed(dataa):
#         # print(i)
#         # swapping_probability=amin + i*stepsize
#         # generation_probability =amin + i*stepsize
#         # print(swapping_probability)
#         data = memb.get_statistics(
#             memory_numbers=memory_numbers,
#             generation_probability=generation_probability,
#             swapping_probability=sw_prob,
#             number_of_repetitions=number_of_repetitions,
#         )

#         while (data[1] / data[0]) > 0.01:
#             number_of_repetitions = 2 * number_of_repetitions
#             # print("new number of repetitions: ", number_of_repetitions)
#             data = memb.get_statistics(
#                 memory_numbers=memory_numbers,
#                 generation_probability=generation_probability,
#                 swapping_probability=sw_prob,
#                 number_of_repetitions=number_of_repetitions,
#             )

#         # Check if the file exists
#         file_exists = os.path.exists(file_name)

#         # Open the CSV file in append mode ('a')
#         with open(file_name, mode="a", newline="") as csvfile:
#             csvfile_writer = csv.writer(csvfile, delimiter=",")

#             # If the file doesn't exist, write the header
#             if not file_exists:
#                 csvfile_writer.writerow(
#                     [
#                         "memory_numbers_list",
#                         "num_segments",
#                         "segment_lengths",
#                         "generation_probability",
#                         "swapping_probability",
#                         "AWT_mean",
#                         "AWT_error",
#                         "number_of_repetitions",
#                         "AWT_ratio",
#                     ]
#                 )

#             # Write the data row
#             csvfile_writer.writerow(
#                 [
#                     memory_numbers_list,
#                     num_segments,
#                     segment_lengths,
#                     generation_probability,
#                     sw_prob,
#                     data[0],
#                     data[1],
#                     number_of_repetitions,
#                     data[1] / data[0],
#                 ]
#             )
