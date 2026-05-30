#0 for Rock
#1 for Paper
#2 for Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("Enter a valid Number!!!")
else:
    print("Your Choice:", user_choice)
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer Choice:", computer_choice)
    print(game_images[computer_choice])
    if user_choice == computer_choice:
        print("It's a Draw 😎")
    elif user_choice == 2 and computer_choice == 0:
        print("YOU LOSE 😑")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN 🎉")
    elif user_choice < computer_choice:
        print("YOU LOSE 😑")
    elif user_choice > computer_choice:
        print("YOU WIN 🎉")