print("Welcome to the Ultimate Mad Libs Game!")
print("Fill in the blanks with the requested words and enjoy your custom story!\n")

# Get user inputs
name = input("Enter a name: ")
friend = input("Enter a friend's name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
food = input("Enter a type of food: ")
emotion = input("Enter an emotion: ")
magical_creature = input("Enter a magical creature: ")
object1 = input("Enter a random object: ")
object2 = input("Enter another random object: ")

# Story template
story = f"""
Once upon a time, {name} and {friend} went on an adventure to {place}. 
The journey was {adjective1} and full of surprises. 

As they walked through the {adjective2} forest, they suddenly heard a strange noise. 
A {animal} appeared out of nowhere and started to {verb1}. 

Just as they were about to run, a {magical_creature} flew down holding a {object1} and said,
'Fear not, brave travelers! You must {verb2} to find the legendary {object2}.'

Excited and a little {emotion}, {name} and {friend} followed the instructions. 
After hours of searching, they finally found it! They celebrated with a feast of {food}. 

And from that day on, they were known as the heroes of {place}. 
The end.
"""

print("\n✨ Here is your story! ✨")

print(story)