#A boring but a intresting one Game on python when you are not on your internet connection
import random
#Random module is a module to generate random results
n = random.randrange(1,100)

user_input = int(input("ENTER YOUR GUESS: "))
# while loop used
while n != user_input:
    if n < user_input:
        print("Too big number you guessed")

        user_input = int(input("ENTER YOUR GUESS AGAIN: "))

    elif n > user_input:
        print("Too small number you guessed")

        user_input=int(input("Enter again Guess number: "))

    else:
        break
        print("You Guessed right!!")
        
