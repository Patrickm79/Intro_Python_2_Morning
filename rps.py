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

while True:

    # User will specify their choice or can type "quit" in order to exit the program
        # How does the program read the user's choice
        # Use python's input function
    users_choice = input("Choose rock, paper, or scissors: ")

    if users_choice == "quit":
        print("See you next time")
        break
    # Program also needs to specify its choice
        # How does the program specify its choice
        # Just have it randomly pick a choice
        # Use Python's random.choice function
    possible_choices = ["rock", "paper", "scissors"]
    programs_choice = random.choice(possible_choices)
    print(f"Program picked {programs_choice}")
    print(f"You picked {users_choice}")

    # Once both choices are made, compare them via rules to see who won
        # How do we do the comparison?
        # use if statments
    if users_choice == "rock":
        if programs_choice == "rock":
            print("A tie!")
            ties += 1
        elif programs_choice == "paper":
            print("Program won!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif users_choice == "paper":
        if programs_choice == "paper":
            print("A tie!")
            ties += 1
        elif programs_choice == "rock":
            print("Program won!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif users_choice == "scissors":
        if programs_choice == "scissors":
            print("A tie!")
            ties += 1
        elif programs_choice == "rock":
            print("Program won!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    else:
        print("I don't understand")
        # go on to the next iteration of the game loop
        continue

    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")