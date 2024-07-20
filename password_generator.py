import random

n=input("press y to generate your 8 letter password \n press q to exit \n enter key :")
while n!="q":

     list=["a","b","c","d","k","l","f","s","h"]
     a1=random.choice(list)
     a2=random.choice(list)
     a3=random.choice(list)
     a4=random.choice(list)
     a5=random.randint(1,9)
     a6=random.randint(1,9)
     a7=random.randint(1,9)
     lis=["@","!","$","&","%"]
     a8=random.choice(lis)
     print("*******************************************************************")
     print("*******************************************************************")
     print("*******************************************************************")
     if n=="y"or n=="Y":
         print("your generated password is :->>> \t",a1,a2,a3,a4,a5,a6,a7,a8)
     else:
         print(" wrong input")
     print("*******************************************************************")
     print("*******************************************************************")
     print("*******************************************************************")
     n=input("press y to generate your 8 letter password \n press q to exit \n enter key :")
print("quitting")         