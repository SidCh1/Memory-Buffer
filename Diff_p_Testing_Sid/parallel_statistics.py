import diff_p_doubling as memb
import scipy.special
import numpy as np
import csv
import os
from concurrent.futures import ProcessPoolExecutor

"""
Goal of this program: 
- Computes waiting times for different swapping_probabilities and distributions of memory_numbers.
- Each segment has different lengths, so different generation probabilities.
- Total distance is fixed, and total memory buffer size is also fixed, but the number of segments can vary.
"""

"""simulation parameters"""

k = 1
b1 = 30
b2 = 20
b3 = 10
b4 = 40
b5 = 25
max_len = k * 200
total_buffer = 32
number_of_repetitions_original = 10
Latt = 22
s1 = k * b1
s2 = k * b2
s3 = k * b3
s4 = k * b4
s5 = k * b5

# Define the new directory for storing CSV files
output_dir = os.path.join(os.path.dirname(__file__), "Data_200k_32b_8seg_a22_all_diff")
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist


# Define the different configurations as a list of dictionaries
configurations = [
    {
        "memory_numbers_list": [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1],
        "segment_lengths": [s2, s2, s1, s1, s1, s1, s2, s2],
        "file_name": "compare_fixed_length_32-8_a22_131_200km.csv",
    },
    {
        "memory_numbers_list": [3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
        "segment_lengths": [s2, s2, s1, s1, s1, s1, s2, s2],
        "file_name": "compare_fixed_length_32-8_a22_313_200km.csv",
    },
    {
        "memory_numbers_list": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        "segment_lengths": [s2, s2, s1, s1, s1, s1, s2, s2],
        "file_name": "compare_fixed_length_32-8_a22_2222_200km.csv",
    },
    # {
    #     "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
    #     "segment_lengths": [s3, s3, s4, s3],
    #     "file_name": "compare_fixed_length_32-4_a22_15_55_44_200km.csv",
    # },
    {
        "memory_numbers_list": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        "segment_lengths": [s5, s5, s5, s5, s5, s5, s5, s5],
        "file_name": "compare_fixed_length_32-8_a22_25_25_2222_400km.csv",
    },
    # {
    #     "memory_numbers_list": [2, 2, 2, 2, 2, 2, 2, 2],
    #     "segment_lengths": [s5, s5, s5, s5],
    #     "file_name": "compare_fixed_length_16-4_a22_25_25_44_400km.csv",
    # },
]


# k = 4
# b1 = 30
# b2 = 20
# b3 = 10
# b4 = 40
# b5 = 25
# max_len = k * 100
# total_buffer = 32
# number_of_repetitions_original = 10
# Latt = 22
# s1 = k * b1
# s2 = k * b2
# s3 = k * b3
# s4 = k * b4
# s5 = k * b5

# # Define the new directory for storing CSV files
# output_dir = os.path.join(os.path.dirname(__file__), "Data_400k_32b_4s_a22_all_diff")
# os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist


# # Define the different configurations as a list of dictionaries
# configurations = [
#     {
#         "memory_numbers_list": [5, 5, 3, 3, 2, 2, 6, 6],
#         "segment_lengths": [s1, s2, s3, s4],
#         "file_name": "compare_fixed_length_32-4_a22_5326_400km.csv",
#     },
#     {
#         "memory_numbers_list": [3, 3, 5, 5, 6, 6, 2, 2],
#         "segment_lengths": [s1, s2, s3, s4],
#         "file_name": "compare_fixed_length_32-4_a22_3562_400km.csv",
#     },
#     {
#         "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
#         "segment_lengths": [s1, s2, s3, s4],
#         "file_name": "compare_fixed_length_32-4_a22_4444_400km.csv",
#     },
#     # {
#     #     "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
#     #     "segment_lengths": [s3, s3, s4, s3],
#     #     "file_name": "compare_fixed_length_32-4_a22_15_55_44_200km.csv",
#     # },
#     {
#         "memory_numbers_list": [4, 4, 4, 4, 4, 4, 4, 4],
#         "segment_lengths": [s5, s5, s5, s5],
#         "file_name": "compare_fixed_length_32-4_a22_25_25_44_400km.csv",
#     },
#     {
#         "memory_numbers_list": [2, 2, 2, 2, 2, 2, 2, 2],
#         "segment_lengths": [s5, s5, s5, s5],
#         "file_name": "compare_fixed_length_16-4_a22_25_25_44_400km.csv",
#     },
# ]


def gen_prob_function(length):
    return np.exp(-length / Latt)


dataa = np.linspace(0.1, 1, 10)  # Swapping probability range


def run_simulation(config):
    memory_numbers_list = config["memory_numbers_list"]
    segment_lengths = config["segment_lengths"]

    # Modify the file path to include the new output directory
    file_name = os.path.join(output_dir, config["file_name"])

    num_segments = len(memory_numbers_list) / 2  # number of segments
    generation_probability = [gen_prob_function(length) for length in segment_lengths]

    # Vary swapping probability
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


if __name__ == "__main__":
    # Run all configurations in parallel
    with ProcessPoolExecutor() as executor:
        executor.map(run_simulation, configurations)
