import pandas as pd
import matplotlib.pyplot as plt

def plot_csv_data(file1, file2):
    # Read data from the first CSV file
    data1 = pd.read_csv(file1)

    # Read data from the second CSV file
    data2 = pd.read_csv(file2)

    # Plot the data from file1
    plt.figure(figsize=(10, 6))

    # Plot data from file1
    x1 = data1['swapping_probability']
    y1 = data1['AWT_mean']
    plt.plot(x1, y1, color='blue', marker='o', linestyle='-', markersize=6)

    # Plot data from file2
    x2 = data2['swapping_probability']
    y2 = data2['AWT_mean']
    plt.plot(x2, y2, color='red', marker='x', linestyle='-', markersize=6)


    # # Plot data from file1
    # for _, row in data1.iterrows():
    #     plt.plot(row['swapping_probability'], row['AWT_mean'], 'o', color='blue')  # Using 'o' for markers

    # # Plot data from file2
    # for _, row in data2.iterrows():
    #     plt.plot(row['swapping_probability'], row['AWT_mean'], 'x', color='red')  # Using 'x' for markers

    # Add a single legend entry for each dataset
    plt.scatter([], [], color='blue', marker='o', label=f'{file1} Data')  # Label for file1 data
    plt.scatter([], [], color='red', marker='x', label=f'{file2} Data')  # Label for file2 data



    # Labels and title
    plt.xlabel('Swapping Probability')
    plt.ylabel('AWT Mean')
    plt.title('Comparison of AWT Mean vs Swapping Probability')

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()

# Main function to run the script
if __name__ == "__main__":
    # Path to your CSV files
    file1 = 'compare_fixed_length_32-4_dl.csv'
    file2 = 'compare_fixed_length_32-un.csv'

    # Call the function to plot data from both CSVs
    plot_csv_data(file1, file2)
