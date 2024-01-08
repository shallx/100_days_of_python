import os
from art import logo
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True

playerWins = 0
dealerWins = 0
draw = 0

def picACard():
    return random.choice(cards)

def printScore(playerHand, computerHand, playerScore, computerScore):
    print(f"Your final hand: {playerHand}, final score: {playerScore}")
    print(f"Computer's final hand: {computerHand}, final score: {computerScore}")

def checkWinCon(playerHand, computerHand):
    playerScore = sum(playerHand)
    computerScore = sum(computerHand)
    if playerScore > 21 or playerScore == 21 or computerScore == 21:
        return True

    return False


def askForCard(playerHand, computerHand):
    while 1:
        s = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if s == "y":
            playerHand.append(random.choice(cards))
            gameEnd = checkWinCon(playerHand, computerHand)

            if not gameEnd:
                print(f"Your cards: {playerHand}, current score: {sum(playerHand)}")
            else:
                break # Game Ends
        
        elif s != "n":
            print("Invalid Selection, try again!")
            askForCard(playerHand, computerHand)
            return
        else:
            return (playerHand)
        
    return playerHand

    



def playBlackJack():
    global playerWins
    global dealerWins
    global draw
    
    cls()
    print(logo)
    playerHand = []
    computerHand = []
    playerHand = [picACard(), picACard()]
    playerScore = sum(playerHand)
    computerHand = [picACard()]
    print(f"Player cards: {playerHand} score {playerScore}")
    print(f"Dealer's first card: {computerHand[0]}")

    hasWon = checkWinCon(playerHand, computerHand)
    if not hasWon:
        playerHand = askForCard(playerHand, computerHand)
        
        computerScore = sum(computerHand)
        playerScore = sum(playerHand)
        while computerScore < 16:
            card = picACard()
            computerHand.append(card)
            computerScore += card

        print("\n")
        printScore(playerHand, computerHand, playerScore, computerScore)
        if playerScore > 21:
            print("You went over. You lose 😭")
            dealerWins += 1
        elif playerScore == 21:
            print("You got a blackjack. You won 🏆")
            playerWins += 1
        elif computerScore == 21:
            print("You lost 😭. Dealer got blackjack")
            dealerWins += 1
        elif computerScore > 21:
            print("Dealer went over. You won 🏆")
            playerWins += 1
        elif playerScore > computerScore:
            print("You Scored more, You won!!")
            playerWins += 1
        elif playerScore == computerScore:
            print("Draw!")
            draw += 1
        else:
            print("Dealer Won")


while should_continue:
    s = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if s == "y":
        playBlackJack()
    elif s == "n":
        should_continue = False
        print(f"You won {playerWins} times | Dealer wins {dealerWins} | Draw {draw}")
    else:
        print("Invalid selection, try again!")
