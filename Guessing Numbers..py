import random

n = random.randrange(1,100)

user_input = int(input("ENTER YOUR GUESS: "))

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
        
