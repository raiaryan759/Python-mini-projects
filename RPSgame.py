import random
def play_game():
    print("Rock Paper Scissors Game")
    print("Enter your choice: rock, paper, or scissors")
    choice = input("Your choice: ").lower()

    randomc = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {randomc}.")

    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")

    elif choice == "rock":
        print("You chose rock.")
        if randomc == "rock":
            print("It's a tie!")
        elif randomc == "paper":
            print("You lose! Paper covers rock.")
        else:
            print("You win! Rock crushes scissors.")

    elif choice == "paper":
        print("You chose paper.")
        if randomc == "rock":
            print("You win! Paper covers rock.")
        elif randomc == "paper":
            print("It's a tie!")
        else:
            print("You lose! Scissors cut paper.")

    elif choice == "scissors":
        print("You chose scissors.")
        if randomc == "rock":
            print("You lose! Rock crushes scissors.")
        elif randomc == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("It's a tie!")
    

while True:
    if __name__ == '__main__':
        play_game()
        ask = input("Do you want to play again? (yes/no): ").lower()
        if ask == "yes":
            print("Restarting the game...")
            
        else:
            print("Thanks for playing! Goodbye.")
            break