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



while(1):
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Siccors\n"))
  
  if user_choice >= 0 and user_choice <=2:
    choices = [rock, paper, scissors]
    print("You chose:")
    print(choices[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose:\n {choices[computer_choice]}")

    # - for loose, 1 for win, 0 for draw
    wincon = [
      [0, -1, 1], # wincon for rock
      [1, 0, -1],
      [-1, 1, 0]
    ]

    win_outputs = ["Draw", "You Win", "You loose"]

    print(f"{win_outputs[wincon[user_choice][computer_choice]]}\n\n")

  else:
    print("You choose an invalid number")