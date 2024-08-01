import random

print("choose rock, paper ou scissors or no to exit:")
input_user = input().lower()
while input_user != 'no':
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose {computer}")
    print(f"User chose {input_user}")

    if input_user == computer:
        print("Tie")
    elif input_user == 'rock':
        if computer == 'scissors':
            print("User wins")
        else:
            print("Computer wins")
    elif input_user == 'scissors':
        if computer == 'paper':
            print("User wins")
        else:
            print("Computer wins")
    elif input_user == 'paper':
        if computer == 'rock':
            print("User wins")
        else:
            print("Computer wins")
    else:
        print("Invalid input")
    print("choose rock, paper ou scissors or no to exit:")
    input_user = input().lower()
    if input_user == 'no':
        break