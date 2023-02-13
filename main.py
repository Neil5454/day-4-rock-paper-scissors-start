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

#Write your code below this line 👇
import random
moves = [rock, paper, scissors] 

user_pick = int(input("What do you chose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
if user_pick >= 3 or user_pick < 0:
  print("You typed an invalid number.  Try again.")
else:
  print(moves[user_pick])

  computer_pick = random.randint(0, 2) #picks random number 0 to 2 from moves list for computer
  print("Computer chose:")
  print(moves[computer_pick])
  
  
  if user_pick == 0 and computer_pick == 2:
    print("You win!")
  elif computer_pick == 0 and user_pick == 2:
    print("You lose!")
  elif computer_pick > user_pick:
    print("You lose!")
  elif computer_pick < user_pick:
    print("You win!")
  elif computer_pick == user_pick:
    print("It's a draw!")
