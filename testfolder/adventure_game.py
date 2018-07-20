# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

while True:
    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        print("You decide to go left and a wall closes off the path you came from. You come across a stairway leading up and down.") # Update to match your story.
        while True:
            print("Type 'up' to go up or 'down' to go down.")
            user_input = input()
            if user_input == "up":
                print("You choose to go up and a rock fell on top of you. You died.")
            elif user_input == "down":
                print("You choose to go down and you enter a cave. You see no other path to take.")
            else: print("Try again!")
    # Continue code to finish story.        

    elif user_input == "right":
        print("You choose to go right and something starts chasing you from behind. You start running and come across a ladder and a hallway.") # Update to match your story.
        while True:
            print("Type 'ladder' to go up the ladder pr 'hallway' to take the hallway")
            user_input = input()
            if user_input == "ladder":
                print("You go up the ladder and escape whatever was chasing you.")
            elif user_input == "hallway":
                print("The thing chasing you catches you in the hallway. You died.")
            else: print("Try again!")
    # Continue code to finish story.

    else: print("Try again!")
