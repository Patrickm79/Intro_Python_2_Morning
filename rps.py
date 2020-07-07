# Write a program to play Rock Paper Scissors with a user
# Let's flesh out the rules and think about how this is going to work


# Rules: Rock -> Scissors
    # Scissors -> Paper
    # Paper -> Rock
import random

# Flow:
# Start up program

wins = 0
losses = 0
ties = 0

# keep all of this going in an infitnite loop until the user decies to quit
# return 0 to indicate a tie, return 1 to indicate user won, return -1 to indicate the computer won
def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    # player wins
    elif (player_choice == "rock" and computer_choice == "scissors") \
        or (player_choice == "scissors" and computer_choice == "paper") \
        or (player_choice == "paper" and computer_choice == "rock"):
        return 1
    # player loses
    else: 
        return -1


possible_choices = ["rock", "paper", "scissors"]
while True:

    # User will specify their choice or can type "quit" in order to exit the program
        # How does the program read the user's choice
        # Use python's input function
    users_choice = input("Choose rock, paper, or scissors: ")

    if users_choice == "quit":
        print("See you next time")
        break
    elif users_choice not in possible_choices:
        print("I don't understand that")
        continue

    # Program also needs to specify its choice
        # How does the program specify its choice
        # Just have it randomly pick a choice
        # Use Python's random.choice function
    
    programs_choice = random.choice(possible_choices)
    print(f"Program picked {programs_choice}")
    
    # Once both choices are made, compare them via rules to see who won
        # How do we do the comparison?
        # use if statments

    result = compare_choices(users_choice, programs_choice)

    if result == 0:
        print("A tie!")
        ties += 1
    elif result == 1:
        print("You won")
        wins += 1
    else:
        print("Computer won!")
        losses += 1

    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")