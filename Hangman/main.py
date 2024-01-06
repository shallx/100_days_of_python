import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Variable declaration
lives = 6
game_over = False
word = random.choice(word_list)
blank_word = []
ln = len(word)
for _ in range(ln):
  blank_word.append("_")

print(logo)
print(blank_word)


# Game loop
while not game_over:
  matched = False
  guess = input("\nGuess a letter:")
  cls() # clear screen

  if guess in blank_word:
    print(f"You already used the letter {guess}")

  else:
    for i in range(ln):
        if word[i] == guess:
            blank_word[i] = guess
            matched = True

    if not matched:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives-=1
    else:
       print("You found one!!\n")

    if lives == 0:
        game_over = True
        print("You lost!")

    elif "_" not in blank_word:
        game_over = True
        print("You win!")
        
  print(blank_word)
  print(stages[lives])

print(f"The word is: {word}")