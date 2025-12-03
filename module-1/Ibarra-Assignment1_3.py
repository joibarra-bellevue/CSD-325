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

# initializing counter will decrease with each iteration of loop
# initializing loop if count is greater than 1
count = bottles

while count >= 1:
    # Will print first half of song with current bottle count if count is greater than 1
    if count > 1:
        print(str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer.")
        print("Take one down and pass it around, " + str(count - 1) + " bottle(s) of beer on the wall.")
    else:
        # Only 1 bottle left. Using last verse of song 
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")

    # Take one bottle away for the next round
    count = count - 1

# When the loop finishes, we are back here in the main program
print("Time to buy more bottles of beer!")
