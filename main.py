#Dice Roll Program 

#import libraries
import sys
import random

#function rolls dice until snake eyes
def snakeEyes(d1, d2):

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    sum = d1 + d2
    print(str(d1) + " - " + str(d2) + " (total = " + str(sum) + ")")

    #set up a while loop 
    while sum != 2:
        snakeEyes(d1, d2)
    else: 
        print("Snake Eyes")
        askMenu()


#function rolls dice n times
def rollDiceN(d1, d2):
    #variable stores user input
    nQ = int(input("How many rolls would you like?"))

    #set up a for loop
    if (nQ >= 0):
        for x in range(0, nQ):
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sum = str(d1 + d2)
            print(str(d1) + " - " + str(d2) + " (total = " + sum + ")")
        else:
            askMenu()
    
    else: 
        print("Please Enter a Valid Number")
        rollDiceN(d1, d2)


#function rolls dice 5 times
def rollDiceFive(d1, d2):
    #set up a for loop
    for x in range(0,5):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        sum = str(d1 + d2)
        print(str(d1) + " - " + str(d2) + " (total = " + sum + ")")
    else:
        askMenu()


#function rolls dice once
def rollDiceOnce(d1, d2): 
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    sum = str(d1 + d2)
    print(str(d1) + " - " + str(d2) + " (total = " + sum + ")")
    askMenu()


#this function will be the main dice function that will call other functions
def diceMaster(userInp):
    #create variables that will store dice 1 and 2
    d1 = None
    d2 = None
    
    if (userInp == 1):
        rollDiceOnce(d1, d2)
    
    elif(userInp == 2):
        rollDiceFive(d1, d2)

    elif(userInp == 3):
        rollDiceN(d1, d2)

    elif(userInp == 4): 
        snakeEyes(d1, d2)
    
    elif(userInp == 5): 
        print("Program Closed")
        sys.exit()
    
    else:
        print("Invalid Response")
        askMenu()


#this function will display the menu and ask the question
def askMenu():
    userInp = int(input("Dice Roll Simulator Menu \n 1. Roll Dice Once \n 2. Rolle Dice 5 Times \n 3. Roll Dice 'n' Times \n 4. Roll Dice until Snake Eyes \n 5. Exit  \n"))
    diceMaster(userInp)
askMenu()
