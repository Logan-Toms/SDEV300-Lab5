"""
This program will allow the user to select a file to analyze and then select a column to analyze. 
The program will display the statistics for the column and then display a histogram of the data in 
the column.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_choice):
    """Load the data from the file and return the dataframe and column names"""
    if file_choice == '1':
        df = pd.read_csv('PopChange.csv') # read the data from the file
        columns = ['Pop Apr 1', 'Pop Jul 1', 'Change Pop'] # create a list of column names
    elif file_choice == '2':
        df = pd.read_csv('Housing.csv') # read the data from the file
        columns = ['AGE', 'BEDRMS', 'BUILT', 'ROOMS', 'UTILITY'] # create a list of column names
    return df, columns # return the dataframe and column names


def display_stats(column, data):
    """Display the statistics for the column"""
    print(f"\nYou selected {column}")
    print("The statistics for this column are:")
    print(f"Count = {data.count()}")
    print(f"Mean = {data.mean().round(2)}")
    print(f"Standard Deviation = {data.std().round(2)}")
    print(f"Min = {data.min()}")
    print(f"Max = {data.max()}")


def plot_histogram(column, data):
    """Plot a histogram of the data in the column"""
    plt.hist(data, bins=10, alpha=0.7) # plot the histogram
    plt.title(f"Histogram of {column}")
    plt.show() # display the histogram


def main():
    """Main function of the program"""
    while True:
        # display the menu
        print("\n****** Welcome to the Python Data Analysis App ******\n")
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")
        file_choice = input()

        # validate the user's choice
        if file_choice not in ['1', '2']:
            if file_choice == '3':
                break
            print("\nInvalid choice, please try again.\n")
            continue

        df, columns = load_data(file_choice) # load the data from the file
        # display the column names
        while True:
            print(f"\nYou have entered {'Population' if file_choice == '1' else 'Housing'} Data.")
            print("Select the Column you want to analyze:")
            for i, column in enumerate(columns, start=1):
                print(f"{chr(96 + i)}. {column}")
            print("z. Exit Column")

            # validate the user's choice
            column_choice = input().lower()
            if column_choice == 'z':
                break

            try: # convert the user's choice to an index
                column_index = ord(column_choice) - 97
                column = columns[column_index]
            except (IndexError, TypeError): # handle invalid choices
                print("\nInvalid choice, please try again.\n")
                continue

            # display the statistics and histogram for the column
            display_stats(column, df[column])
            plot_histogram(column, df[column])

    # display the exit message
    print("\n****** Thanks for using the Data Analysis App ******\n")


main()
