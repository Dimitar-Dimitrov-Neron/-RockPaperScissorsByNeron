import random
# Players Move
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose: [r]ock, [p]aper or [s]cisors: ")
computer_move = ""
# Players moves with possible options
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")
# Computer moves
computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
    print(f"The computer chose {rock}.")
elif computer_random_number == 2:
    computer_move = paper
    print(f"The computer chose {paper}.")
else:
    computer_move = scissors
    print(f"The computer chose {scissors}.")
# Possible results
if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
