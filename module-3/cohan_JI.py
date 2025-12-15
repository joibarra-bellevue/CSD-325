"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

If player rolls a 2 or a 7 they get 10 mon bonus!
''')

def isSum2Or7(dice1, dice2, purse):
    sum_dice = dice1 + dice2
    if sum_dice == 2 or sum_dice == 7:
         print('The total roll was', sum_dice)
         print('You receive a 10 mon bonus!')
         purse = purse + 10

purse = 20
while True:  # Main game loop.
    # Place your bet:
    #Added my initials with a colon to input prompt ji:
    print('You have', purse, 'mon. How much do you bet? (or QUIT) ji: ')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1,1)
    dice2 = random.randint(1,1)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)
    
    isSum2Or7(dice1, dice2, purse)

    
    
    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
         print('You won! You take', pot, 'mon.')
         purse = purse + pot  # Add the pot to player's purse.

         house_fee = pot * 12 // 100
         print('The house collects a', house_fee, 'mon fee.')
         purse = purse - house_fee
    else:
             purse = purse - pot  # Subtract the pot from player's purse.
             print('You lost!')
    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
