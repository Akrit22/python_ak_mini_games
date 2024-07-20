
import random

n=int(input("enter n (to place bet on big or small) 1-9 : "))
while n!=0 and n<10:

    p= random.randint(1,9)
    print("generated number is : ",p)
    if n<6 and n>0:
        if p<6 and p>0:
            print("small")
            print("you have won the bet")
        else:
            print("lost the bet")
    elif n<10 and n>5:
        if p<10 and p>5 :
            print("big")
            print("you have won the bet")
        else:
            print("lost")
    else:
        print("entered wrong number")
    print("##########################")
    print("##########################")    
    print("##########################")    
    
    n=int(input("enter n (to place bet on big or small) 1-9 : "))
print("wrong number")

             