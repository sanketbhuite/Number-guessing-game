import random

def number_guessing_game():
    min_ = 1
    max_ = 100
    secret_ = random.randint(min_, max_)
    max_attempts = 10
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between " + str(min_) + " and " + str(max_) + ".")
    print("You have " + str(max_attempts) + " attempts to guess the number.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Attempt " + str(attempts + 1) + ": Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue      
        attempts += 1

        
        if guess < secret_:
            print("Too low!")
        elif guess > secret_:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number " + str(secret_) + " in " + str(attempts) + " attempts.")
            break
    else:
        print("Sorry, you've used all " + str(max_attempts) + " attempts. The number was " + str(secret_) + ".")

number_guessing_game()
