import random

target = random.randint(1, 100)
i = 10

while i > 0:
    userchoice = input(f"Guess the number or Quit (Attempts remaining: {i}): ")
    if userchoice == "Q":
        break
    userchoice = int(userchoice)
    if userchoice == target:
        print("Congratulations")
        break
    elif userchoice < target:
        print("Clue: your number is too small. Try again")
    else:
        print("Clue: your number is too big. Try again")
    i -= 1

print("-----GAME OVER-----")
