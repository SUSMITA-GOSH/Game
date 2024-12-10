import random

Option = ("rock", "paper", "scissors")
Playing = True

while Playing:
    player = None
    computer = random.choice(Option)

    while player not in Option:
        player = input("Enter Your Choice (rock/paper/scissors): ").lower()
    print(f"Player: {player}")   
    print(f"Computer: {computer}")

    if player == computer:
        print("That's a tie!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    else:
        print("--YOU LOSE--")
        
    again = input("Do you want to continue? (y/n): ").lower()
    if again != "y":
        Playing = False

print("Thanks for playing!")
