import random

def welcome(n):

    p=random.randint(1,3)
    if n==1:
        if p==2:
            print("computer : paper")
            print("you win")
        elif p==1:
            print("computer : scissor")    
            print("draw \n ")
        else:
            print("computer : rock")
            print("computer wins\n you lost") 
    elif n==2:
        if p==2:
            print("computer : rock")
            print("you win")
        elif p==1:
            print("computer : paper")    
            print("draw \n ")
        else:
            print("computer : scissor")
            print("computer wins\n you lost") 
    elif n==3:
        if p==2:
            print("computer : scissor")
            print("you win")
        elif p==1:
            print("computer : rock")    
            print("draw \n ")
        else:
            print("computer : paper")
            print("computer wins\n you lost")   
    else:
        print("entered n have not any function") 
    return 1  
print("\t\t\t\t\t\t  WELCOME TO THE GAME ")
print("\t\t\t\t\t\tInstruction")
print("\t\t\t\t\tIn the rock paper scissor game ")
print("\t\t\t\t\tyou will be given three option")
print("\t\t\t\t\tyu can select one of the three option ")
print("\t\t\t\t\tto play the game.")
print("\t\t\t\t\tselect 1 for scissor")
print("\t\t\t\t\tselect 2 for paper")
print("\t\t\t\t\tselect 3 for rock")
print("\t\t\t\t\t\t*******************************")
print("\t\t\t\t\tpress 1 to start")
print("\t\t\t\t\tpress 9 to quit ")
print("\t\t\t\t\t\t*******************************")
num=int(input(f"\t\t\t\t\tenter key : "))
if num==1:

    print("enter\n 1 for scissor \n 2 for paper \n 3 for rock")
    n=int(input("you: enter n : "))
    while n<4 and n>0:
        welcome(n)
        print("\t\t\t\t\t\t*******************************")
        print("\t\t\t\t\tpress 1 to continue")
        print("\t\t\t\t\tpress 9 to quit ")
        num=int(input(f"\t\t\t\t\tenter key : "))
        if num ==9:
            print("exit")
            break

        print("enter\n 1 for scissor \n 2 for paper \n 3 for rock")
        n=int(input("you: enter n : "))  
else:
    print("you have pressed wrong key")        