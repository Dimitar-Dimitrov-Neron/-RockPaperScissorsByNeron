import random

running = True

print("=" * 50)
name = (input("Enter your name: "))
print("=" * 50)
print(f"                Greetings {name}")
print("=" * 50)

while running:
    # Players Move
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    player_points = 0
    computer_points = 0
    player_move = input("Choose: [r]ock, [p]aper or [s]cissors: ")
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
        player_points += 1
        player_points = player_points
        print(f"Your score is: {player_points} points.")
    elif player_move == computer_move:
        print("Draw!")
        player_points = player_points
        computer_points = computer_points
        print(f"Your score:{player_points}")
        print(f"Computer score:{computer_points}")
    else:
        print("You lose!")
        computer_points += 1
        computer_points = computer_points
        print(f"Computer score: {computer_points} points.")

    print("=" * 50)
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
