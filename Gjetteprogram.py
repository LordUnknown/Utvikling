import random

posibilities = ["1","2","3","4","5","6","7","8","9","10"]

answer = random.choice(posibilities)
attempts = 3
success = 0
score = 0


print("Your objecive is to guess a randomly generated number between 1-10, you will start with 3 attempts. Good luck.")

while attempts > 0:
    print("You have", attempts, " attempts left to guess a number of 1-10")
    guess = input("What is your guess? ")
    if guess == answer:
        print("Congratulations, you guessed the right number!")
        success = 1
    elif guess >= answer:
        print("Try a lower number, my friend ;)")
        attempts -= 1
    elif guess <= answer:
        print("Try a higher number, my friend ;)")
        attempts -= 1
    if attempts == 0:
        if input("You unfortunatly used all your attempts, would you like to try again? YES/NO. ") == "YES":
            print("Thank you for countinuing")
            answer = random.choice(posibilities)
            attempts = 3
            success = 0
        else:
            print("Goodbye, then. Your final Score was ", score)
            exit()
    if success == 1:
        if input("You guessed the correct number, would you like to try again? YES/NO. ") == "YES":
            print("Thank you for contuing playing.")
            answer = random.choice(posibilities)
            attempts = 3
            success = 0
            score += 1
            print("Your current score is ", score)
        else:
            print("Goodbye, then. Your final Score was ", score)
            exit()
            