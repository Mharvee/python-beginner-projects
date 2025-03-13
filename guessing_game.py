import random
number = random.randint(1, 100)
print("Welcome to the number guessing game")
difficulty = input("Choose your difficulty E for easy H for hard ").lower()
tries = 0
if difficulty == "e":
    tries = 12
elif difficulty == "h":
    tries = 5
print(f"Guess a number between 1 and 100. Keep in mind you have just {tries} tries ")
while tries>0:
    Guess = int(input("Enter your guess "))
    if Guess < number:
        print("Too low try again")
        tries-=1
    elif Guess > number:
        print("Too high try again")
        tries-=1
    elif Guess == number:
        print(f"Well done you guessed {number} correctly")
        break
    else:
        print("Invalid input")

    if tries>0:
        print(f"You have only {tries} tries left")
if tries == 0:
    print(f"Game over the correct number was {number}")
