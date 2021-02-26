# This is classwork

#We're going to create our first video game with Python! A Simple game of Rock, Paper, Scissors, played by two players - the user, and the "computer opponent" (your Python program)

# Your goal is to execute a single round of Rock, Paper, Scissors. This means that you need to let a user enter which of these three values they'd like to "play" this round, and you need to randomly select an option for the computer/opponent to play.


#Its going to be person versus computer is going to pick randomly.

import random

#Take User Input
user_action = input("Enter a choice (rock, paper, scissors): ")
# Make the Computer Choose
possible_actions = ["rock", "paper", "scissors"]

computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Deciding who is going to win based on the the choices. I am using the if, elif,and else block to compare players’ choice. 

# I am using the if, elif,and else block to determin a tie, win 




if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# A single game of rock paper scissors is quite fun, were going to try several games in a row

import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
# "y" to play again and "n" to play no more. 

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break