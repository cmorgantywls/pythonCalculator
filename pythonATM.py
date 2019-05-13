import math
import random


useATM = False
balance=random.randint(100,100000)

def setPIN():
    # to add later - make sure that PIN must be a four digit numeric value.
    # either do some fancy string stuff or just make sure it falls between 1000 and 9999 IDK!
    thePIN=int(input("Set your ATM PIN to access your account.\n"))
    return thePIN
    
def checkPIN(thePIN):
    enteredPIN=int(input("Great! Enter your PIN again to get started.\n"))
    while enteredPIN!=thePIN:
        enteredPIN=int(input("That's not your PIN. Try entering your four digits again.\n"))
    
    if (thePIN==enteredPIN):
        return True

def getUserChoice():
    userChoice=int(input("Welcome to your ATM! What would you like to do?\n1:Check Balance\n2:Make Deposit\n3:Make Withdrawal\n4:Leave ATM\n"))
    return userChoice

def checkBalance(balance):
    print(f'Your current balance is ${balance}')
    
def makeDeposit(balance):
    correctDeposit=False
    
    while correctDeposit==False:
        theDeposit=int(input("How much would you like to deposit?\n"))
        try:
            if theDeposit>0:
                balance += theDeposit
                print(f'Your new balance is ${balance}.')
                correctDeposit=True
                return balance
            else:
                print("That is not a valid amount. Remember, you must enter your value numerically and cannot make negative deposits.")
        except ValueError:
            # this also does a weird thing IDK!!!
            print("You must enter a number.")
    
def makeWithdrawal(balance):
    correctWithdrawal=False
    
    while correctWithdrawal==False:
        theWithdrawal=int(input("How much would you like to withdraw?\n"))
        # just honestly too tired to keep messing with try except rn
        if theWithdrawal>0 & theWithdrawal< balance:
            balance-=theWithdrawal
            correctWithdrawal=True
            return balance
        else:
            print(f'That is not a valid amount.\nPlease enter a numeric amount greater than 0 and less than ${balance}.')
        
def exitATM():
    confirmation = input("Enter y if you would like to exit the ATM.")
    if confirmation.lower() == "y":
        print("Thanks for coming by!")
        return False
    else:
        print("Continue using ATM, okay!")
        return True
    
        
thePIN=setPIN()
useATM=checkPIN(thePIN)

while useATM==True:
    userChoice=getUserChoice()
    try:
        if userChoice==1:
            checkBalance(balance)
        elif userChoice==2:
            makeDeposit(balance)
        elif userChoice==3:
            makeWithdrawal(balance)
        elif userChoice==4:
            useATM=exitATM()
        else:
            print("That is not a valid choice. Please enter a number 1 through 4 to make a selection.")
    except ValueError:
        # why isn't this happening? >:(
        print("Please enter a number to make your selection.")
        
print("To access ATM again, please enter your PIN number.")
useATM=checkPIN(thePIN)