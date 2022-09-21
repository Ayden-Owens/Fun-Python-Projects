# Made this to help with DND 
# I want to improve this dice roller and have a print statement that asks the user to for damage.
# Then the program adds up the damage. Or roll for initiative


from operator import truediv
from random import random, randrange        

def roll_dice(dice_num):
    number = randrange(1, dice_num)
    if (number == 1):
        nat1 = "You rolled a natural 1!"
        print(nat1)
    elif(number == 20):
        nat20 = "You rolled a natural 20!"
        print(nat20)
    else: 
        print("You rolled a {} ".format(number))

def coin_flip():
    num = randrange(1,3)
    if (num == 1):
        print("Heads!")
    else:
        print("Tail!")

def dice():
    roll = True
    while (roll):
        message = "Enter the dice you want to roll"
        print(message)
        die = input()
        try:
            die_num = int(die)
            if(die_num == 1) or (die_num == 2):
                print("You cannot roll a dice that only has one or two sides. Reroll!")
            else:
                roll_dice(die_num)
        except ValueError:
            print("Please put a number in from 3 to above!")

def split(word):
    return [char for char in word]
    
def isNumber(input):
    list = split(input)
    for x in list:
        if(x.isnumeric()):
            #print("This is a number {}".format(x))
            return True
        else:
            continue
            #print("This is not a number {}".format(x))
    return False
    
def isCharacter(input):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in input):
        return True
    else:
        return False
    
def string_check(message):
    reset = True
    while (reset):
        print(message)
        r = input()
        if (isNumber(r) == True):
            print("Numbers are not valid inputs")
            reset = True
        else:
            if (isCharacter(r) == True):
                print("Special characters are not valid inputs")
                reset = True
            else:
                reset = False
    return r

def input_check(message):
    again = True
    while(again):
        print(message)
        num = input()
        try:
            val = int(num)
            again = False
        except ValueError:
            print("This is not a number. Please enter a valid number")
            again = True
    return val 
        
retry = True
while(retry):
    message = "Enter flip to flip a coin or enter roll to roll a dice!"
    user = string_check(message)
    if (user == "flip"):
        coin_flip()
    elif (user == "roll"):
        message = "Enter how many die you want to roll"
        num1 = input_check(message)
        output = "Enter which type of dice you want to roll"
        num2 = input_check(output)
        for x in range(num1):
            roll_dice(num2)
    elif (user == "exit"):
        print("Time to go")
        quit()
    else:
        print("I'm sorry please type filp, roll, or exit")
        
    
                        
    


