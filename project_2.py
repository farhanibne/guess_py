import random

secret_number = random.randint(1,100)
user_guess = None
guess = 0



print("\t\t welcome to dz guess game. thank you for entering over here.a thumbs up for you!!")
print("\t\t randomly numbers 1-100 will be generated")
print("\t\t you just have to guess")
print("\t\t do it you  are  a brilliant")


# print("\t\t",secret_number)


while(user_guess != secret_number):
    user_guess = int(input("\t\t enter the random number :  "))
    guess += 1
    if(user_guess==secret_number):
        print("\t\t You guess the right!! Brilliant work!!!")
    else:
        if(user_guess > secret_number):
            print("\t\t Wrong!!. Please give a less ammount of number")
        else:
            print("\t\t Wrong!!. Please give a larger number")    

   


print(f"\t\t yepp.you guess the number in {guess} guess")
   
   
   
   
