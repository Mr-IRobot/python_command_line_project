
print("Hello! Welcome to the quiz game")
play = input("Do you want to play? ")

if play.lower() != "yes":
    print ("Quiz ended")
    quit()


score = 0
print ("okay! let's begin")


print ("Question 1")
Answer = input("what does CPU stands for? ")
if Answer.lower() == "central processing unit":
    print("Correct! :)")
    score += 1
else:
    print ("Incorrect!")
    correction = input("Do you want to know the correct answer? ")
    if correction.lower() != "yes":
        print("Okay! Moving to the next question")
    print ("CPU stands for central processing unit")



print ("Question 2")
Answer = input("what does GUI stands for? ")
if Answer.lower() == "graphics user interface":
    print("Correct! :)")
    score += 1
else:
    print ("Incorrect!")
    correction = input("Do you want to know the correct answer? ")
    if correction.lower() != "yes":
        print("Okay! Moving to the next question")
    print ("GUI stands for graphics user interface")



print ("Question 3")
Answer = input("what does IDE stands for? ")
if Answer.lower() == "integrated development environment":
    print("Correct! :)")
    score += 1
else:
    print ("Incorrect!")
    correction = input("Do you want to know the correct answer? ")
    if correction.lower() != "yes":
        print("Okay! Moving to the next question")
    print ("IDE stands for integrated development environment")



print ("Question 4")
Answer = input("what does CSS stands for? ")
if Answer.lower() == "cascading style sheet":
    print("Correct! :)")
    score += 1
else:
    print ("Incorrect!")
    correction = input("Do you want to know the correct answer? ")
    if correction.lower() != "yes":
        print("Okay! Moving to the next question")
    print ("CSS stands for cascading style sheet")
    
if score <= 2:
    print("Failed! pls try again")
else:
    print("Congratulations! you passed")

print("Your score is " + str(score) + "(" + str((score/4)*100) + "%." + ")")
