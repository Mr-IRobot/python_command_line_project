
import random

print("You are to guess a number equivalent to the one displayed by the computer")

top_range = input("Type the range of number you want to guess | ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("pls type a number greater than zero")
        quit()

else:
    print("Pls type a number")
    quit()

random_number = random.randint(1, top_range)
guess = 0

while True:
    guess += 1
    guessed_number = input("Guess a number between 0 and "+ str(top_range)+ " | ")
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)

        if guessed_number <= 0:
            print("Your guess is lower than zero, try again")
            continue
        else:
            print("Wait a moment let's check if your guess is correct")

    else:
        print("Pls type a number and try again")
        continue

    if guessed_number == random_number:
        print("Congratulations! Your guess was correct")
        break
    elif guessed_number < random_number:
        print("Wrong! Your guess was below the number, Pls try again")
        continue
    else:
        print("Wrong! Your guess was above the number, Pls try again")
        continue
    
print("You got it in", guess, "guesses.")


 