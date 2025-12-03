#Jorge Ibarra
#CSD-325 12/3/2025
#Assignment 1.3
#This code will ask user for input and and prit lyrics to a popular song. With each iteration bottle count will be reduced by 1 until bottle count is 0. Program will print final lyric and terminate. 


#defining song_lyrics function that will be called in the main code. Will loop through while count is greater than or equal to 1.
def song_lyrics(start_bottles):
    count = start_bottles
    while count >= 1:
        if count > 1: #printing these lyrics if bottle count is greater than 1. 
            print(str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer.")
            print("Take one down and pass it around, " + str(count - 1) + " bottle(s) of beer on the wall.")
            print()  
        else: #Printing these lyrics once bottle count reaches 1
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            print()

        # Decrease the count for the next iteration
        count = count - 1


#validating user input only positive numbers, less than 100, and numbers only
while True:
    bottles = input("Enter number of bottles: ")
    try:
        bottles = int(bottles)
        if bottles > 0 and bottles <= 100:
            break
        else:
            print("Number must be greater than 0 and less than or equal to 100:")
            print()
    except ValueError:
        print("Try again. Enter a number:")
        print()
# Fabio Musanni – Programming Channel. (2022). How to validate user inputs in Python | Input validation in Python [Video]. YouTube. https://youtu.be/LUWyA3m_-r0

# Calling song_lyrics function and passing current bottle count
song_lyrics(bottles)

# Will print once bottle count reaches 0
print("Time to buy more bottles of beer!")