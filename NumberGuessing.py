from random import random, randrange
import random

def begin():
    again = True
    while(again):
        user_input = input()
        if(user_input.isnumeric()):
            message = "Please do enter a number. " + user_input + " is not a valid entry. " + " Press enter start first then you can enter a number."
            print(message)
            again = True
        elif(user_input == "start"):
            message = "Great Let's begin!"
            print(message)
            again = False
        elif(user_input == "end"):
            message = "Bye, Bye!"
            print(message)
            quit()
        else:
            message = "Please enter start or stop any other"
            print(message)
            again = True
                                            
def input_check():
    again = True
    while(again):
        num = input("Please enter a number ")
        try:
            val = int(num)
            again = False
        except ValueError:
            print("This is not a number. Please enter a valid number")
            again = True
    return val 

def hint_one(cpu_number):
    if(cpu_number%2==0):
        print("The cpu number is even")
    else:
        print("The cpu number is odd")

def hint_two(cpu_number):
    if(cpu_number%10 == 0):
        print("The cpu number is a multiple of 10")
    else:
        print("The cpu number is not a multiple of 10")

def hint_three(cpu_number):
    print("The number is one of these numbers!")
    randomlist  = []
    for i in range(10):
        n = randrange(1,100)
        randomlist.append(n)
    randomlist.append(cpu_number)
    random.shuffle(randomlist)
    print(randomlist)
        
def hint_four(cpu_number, user_number):
    num = (cpu_number + user_number) - 3
    print("Time to test your arthemtic. The cpu number is equal to {} plus 3, then subtract the number you typed in which was {}".format(num, user_number))  

def score(cpu_number, user_number):
    if (cpu_number<user_number):
        print("Yes humans win!")
    elif (cpu_number==user_number):
        print("Tie")    
    else:
        print("Booo! cpu wins and humans lose!")

title = "Number Guessing Game!"
game = True
while(game):
    print(title)
    print("Please enter start to start the game or enter end to end the game")
    user_input = input()
    if(user_input.isnumeric()):
        message = "Please do not enter a number. " + user_input + " is not a valid entry. " + " Press start first then you can enter a number."
        print(message)
        again = True
    elif(user_input == "start"):
        message = "Great Let's begin!"
        print(message)
        cpu_number = randrange(1,100)
        round = 0
        cpu_count = 0
        user_count = 10
        message = "Your score right now is 10 and the cpu's score is 0. Each the hint you get the cpu gets points and you the user lose points try to beat the computer!"
        print(message)
        on = True
        while(on):
            intro = "Please enter a number between 1-100!"
            user_num = input_check()
            if (user_num == cpu_number):
                print("GG")
                print("User score:  " + str(user_count) + " and the Cpu score: " + str(cpu_count))
                score(user_num,cpu_number)
                on = False
            elif(user_num<1) or (user_num>100):
                print("invalid entry")
            else:
                round = round + 1
                if(round == 1):
                    hint_one(cpu_number)
                    cpu_count=cpu_count+1
                    user_count=user_count-1
                    on = True
                elif(round == 2):
                    hint_two(cpu_number)
                    cpu_count=cpu_count+1
                    user_count=user_count-2
                    on = True
                elif(round == 3):
                    hint_three(cpu_number)
                    cpu_count=cpu_count+1
                    user_count=user_count-3
                elif(round == 4):
                    hint_four(cpu_number, user_num)
                    user_count=user_count-3
                    cpu_count=cpu_count+3
                    on = True
                else:
                    print("No more hints, Sorry!")
                    print("User score: {} and the Cpu score: {}".format(cpu_count, cpu_count))
                    score(user_num,cpu_number)
                    on = False
    elif(user_input == "end"):
        message = "Bye, Bye!"
        print(message)
        quit()
    else:
        message = "Please enter start or end"
        print(message)
    again = True


            
            
            
        