import random

level = input("Choose a difficulty level (easy, medium, hard): ").lower()

if level == "easy":
    number = random.randint(1, 50)
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number between 1 and 50. Good luck!\n")
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts -= 1
    print(f"The guess was {number}")

        
if level == "medium":
    number = random.randint(1, 100)
    attempts = 7
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number between 1 and 100. Good luck!\n")
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts -= 1

if level == "hard":
    number = random.randint(1, 200)
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number between 1 and 200. Good luck!\n")
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts -= 1
