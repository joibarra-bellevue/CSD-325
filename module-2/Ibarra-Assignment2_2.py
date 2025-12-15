#Jorge Ibarra
#12/10/2025
#Assingment 2.2 
#This program will assk the user to enter numbers. The loop is hard coded with a cutoff at 3 iterations. Program will create an array to store the input. 
# Low, high, sum, and average of the inputted numbers is calculated and printed. 


#declaring an analysis function with all the code required inside of it
def input_analysis():
    numbers = []
    #defining how many times the user will be asked for input 
    
    for a in range(3):
        number= int(input(f"Enter number {a+1}: "))
        numbers.append(number)

   #prining assignment requirements using Python built in functions min/max/sum
    print("Low number: " + str(min(numbers)))
    print("Highest number: " + str(max(numbers)))
    print("Sum: " + str(sum(numbers)))

    #calculating average of all numbers entered 
    average = (sum(numbers)/3) 
    #printing average 
    print("Average: " + str(average))
    

#declaing main function and calling my function in it
def main(): 
    input_analysis()
#executing code with cal to main funciton
main()