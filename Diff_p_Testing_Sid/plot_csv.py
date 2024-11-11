import pandas as pd
import matplotlib.pyplot as plt
import os
import itertools


def plot_csv_data(file_list):
    # Define color and marker options
    colors = itertools.cycle(["blue", "red", "green", "purple", "orange", "cyan"])
    markers = itertools.cycle(["o", "x", "^", "s", "D", "*"])

    plt.figure(figsize=(10, 6))

    for file in file_list:
        # Read data from the CSV file
        data = pd.read_csv(file)
        # Extract memory_numbers_list and segment_lengths from the first row
        memory_numbers = data["memory_numbers_list"].iloc[0]
        segment_lengths = data["segment_lengths"].iloc[0]

        # Plot data with unique color and marker
        color = next(colors)
        marker = next(markers)
        x = data["swapping_probability"]
        y = data["AWT_mean"]
        plt.plot(x, y, color=color, marker=marker, linestyle="-", markersize=6)

        # Add a legend entry
        plt.scatter(
            [],
            [],
            color=color,
            marker=marker,
            label=f"memory_numbers_list={memory_numbers}, segment_lengths={segment_lengths}",
        )

    # Labels and title
    plt.xlabel("Swapping Probability")
    plt.ylabel("AWT Mean")
    plt.title("AWT Mean vs Swapping Probability")

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()


# Main function to run the script
if __name__ == "__main__":
    # Path to your CSV files
    # path = "/Users/thaslimjaglurbasheer/Documents/Siddhu/Memory_Buffer/memory-buffer/Diff_p_Testing_Sid"
    path = "/home/siddhu/Documents/lina_project/memory-buffer/Diff_p_Testing_Sid/Data_test_dl"
    # List of CSV files
    csv_files = [
        # 'compare_fixed_length_32-4_20_40_37.csv',
        # 'compare_fixed_length_32-4_20_40.csv',
        # 'compare_fixed_length_32-4_40_20_73.csv',
        # "compare_fixed_length_32-4_a11_20_40_44_200km.csv",
        # "compare_fixed_length_32-4_a11_20_40_37_200km.csv",
        # "compare_fixed_length_32-4_a11_25_25_44_200km.csv",
        # "compare_fixed_length_16-4_a11_25_25_44_200km.csv",
        "compare_fixed_length_16-4_a22_25_25_44_100km.csv",
        "compare_fixed_length_32-4_a22_25_25_44_200km.csv",
        # "compare_fixed_length_32-8_a22_313_200km.csv",
        # "compare_fixed_length_32-8_a22_2222_200km.csv",
    ]

    file_list = [os.path.join(path, file) for file in csv_files]

    # Call the function to plot data from all CSVs
    plot_csv_data(file_list)
