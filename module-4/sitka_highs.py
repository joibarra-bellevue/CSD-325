#Jorge Ibarra
#CSD325
#Module 4.2 Assignment 
#12/30/2025


# This program allows the user to choose between viewing high or low temperature data
# from a CSV file containing Sitka weather data for 2018.


import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Function to get user choice and validate input - JI 
def getUserInput():
    "Prompt the user to choose between high or low temperatures or to quit."
    while True:
        #Variable will store user input - JI
        choice = input("Enter 'H' to view high temperatures, 'L' to view low temperatures, or 'Q' to quit: ")
        choice = choice.upper() #Input will be capitalized
        
        if choice == 'H' or choice == 'L' or choice == 'Q':
            return choice
        else:
            #User will be asked to re-enter if input is invalid - JI
            print("Invalid entry. Please enter only 'H', 'L', or 'Q'.")
            
#Function to load weather data from the CSV file - JI
def weatherData(filename):
    dates, highs, lows = [], [], []
    #Added ability to read low temperatures - JI
    
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  
        
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
            
    #Return both high and low temps - JI
    return dates, highs, lows

#Main function to run the program and print instructions - JI
def main():
    filename = 'sitka_weather_2018_simple.csv'
    print('This program displays high or low temperature data for Sitka in 2018 in a graph. Enter H for highs or L for lows. Enter Q to exit program')
    
    #loop will continue until user decides to quit - JI
    while True:
        choice = getUserInput() 
        if choice == 'Q':
            print("Goodbye! Thanks for using the weather viewer.")
            break
        #weather data from csv 
        dates, highs, lows = weatherData(filename)  
        
        
        fig, ax = plt.subplots()
        if choice == 'H':
            ax.plot(dates, highs, c='red')
            plt.title("Daily High Temperatures - 2018", fontsize=24)
        elif choice == 'L': #Added option for low temps - JI
            ax.plot(dates, lows, c='blue')
            plt.title("Daily Low Temperatures - 2018", fontsize=24)
        #Creating low temp chart with blue line 
        
        # Format the plot 
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        #dsplay the plot to user
        plt.show()

# Run the program - JI
main()