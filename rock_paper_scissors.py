import random
user_points = 0
computer_points = 0
options = ["s","p","r"]
print("Welcome to the rock paper scissors game")
while user_points < 5 and computer_points < 5:
    user_choice = input("Enter your choice r for Rock, p for Paper or s for scissors ").lower()
    if user_choice not in options:
        print("Invalid choice! Please enter 'r', 'p', or 's'.")
        continue
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("Oh no a draw")
        print(f"No points added, You have {user_points} point(s) ,Computer has {computer_points} point(s)")
    elif (user_choice == "r" and computer_choice == "s" )or \
        (user_choice == "s" and computer_choice == "p" )or \
        (user_choice == "p" and computer_choice == "r"):
        user_points+= 1
        print(f"Yay You won the computer chose {computer_choice}")
        print(f"You have {user_points} point(s) and the computer has {computer_points} point(s)")
    else:
        computer_points+=1
        print(f"You lost the computer chose {computer_choice} and you chose {user_choice}")
        print(f"The Computer has {computer_points} point(s) and you have {user_points} point(s)")

if user_points == 5:
    print("Game over you won")
else:
    print("Game over the computer won")
