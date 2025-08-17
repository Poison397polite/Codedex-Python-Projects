"""Program to play a simplified version of blackjack"""

import random
import time

deck = {
    "A♣" : 11, "2♣" : 2, "3♣" : 3, "4♣" : 4, "5♣" : 5, "6♣" : 6, "7♣" : 7,
    "8♣" : 8, "9♣" : 9, "10♣" : 10, "J♣" : 10, "Q♣" : 10, "K♣" : 10,
    "A♠" : 11, "2♠" : 2, "3♠" : 3, "4♠" : 4, "5♠" : 5, "6♠" : 6, "7♠" : 7,
    "8♠" : 8, "9♠" : 9, "10♠" : 10, "J♠" : 10, "Q♠" : 10, "K♠" : 10,
    "A♦" : 11, "2♦" : 2, "3♦" : 3, "4♦" : 4, "5♦" : 5, "6♦" : 6, "7♦" : 7,
    "8♦" : 8, "9♦" : 9, "10♦" : 10, "J♦" : 10, "Q♦" : 10, "K♦" : 10,
    "A♥" : 11, "2♥" : 2, "3♥" : 3, "4♥" : 4, "5♥" : 5, "6♥" : 6, "7♥" : 7,
    "8♥" : 8, "9♥" : 9, "10♥" : 10, "J♥" : 10, "Q♥" : 10, "K♥" : 10,
}

suits = {
    "♠": "Spades",
    "♥": "Hearts",
    "♦": "Diamonds",
    "♣": "Clubs"
}

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

asciiCards = {}

for suit in suits:
    for rank in ranks:
        asciiCard = [
            "┌─────────┐",
            f"│{rank:<2}       │",  # rank left aligned
            "│         │",
            f"│    {suit}    │",   # suit centered
            "│         │",
            f"│       {rank:>2}│",  # rank right aligned
            "└─────────┘"
        ]
        asciiCards[f"{rank}{suit}"] = asciiCard

def printHand(hand, cards):
    """Prints a list of ASCII cards side by side"""
    # Each card is 7 lines tall
    for row in range(7):
        print(" ".join(cards[c][row] for c in hand))

def shuffleDeck(sDeck):
    """Function to shuffle the deck"""
    # List of the items in the deck dictionary used for shuffling
    items = list(deck.items())

    random.shuffle(items)

    sDeck.clear()
    sDeck.update(dict(items))

def drawCard(hand):
    """Function to draw a card from the deck"""
    card, value = shuffledDeck.popitem()
    hand.append((card, value))

def hasAces(hand):
    """Functions that returns True if there is any aces in the hand and false otherwise"""
    return any(value == 11 for _, value in hand)

def getTotal(hand):
    """Function to get the total of all cards in the hand
    and converts aces to 1 if a bust would occur"""
    aces = sum(value[1] == 11 for value in hand)
    total = sum(value[1] for value in hand)

    while total > 21:
        if aces >= 1:
            total -= 10
            aces -= 1
        else:
            break

    return total

def playAgain():
    """Function to determine if the user wants to keep playing.
    Returns True if yes and False if no"""
    return input("Do you want to play again? y for yes anything else for no: ").lower() == "y"

def printDetails(dHand, pHand, stand = 0):
    """Function to display the hands of the dealer and the player"""
    if stand == 0:
        print("\nThe dealer is showing:")
        printHand([dHand[0][0]], asciiCards)
        print(f"Total of {dHand[0][1]}\n")

        print("You have:")
        printHand([card[0] for card in pHand], asciiCards)

        print(f"Total of {getTotal(pHand)}\n")
    else:
        print("\nThe dealer has:")
        printHand([card[0] for card in dHand], asciiCards)

        print(f"Total of {getTotal(dHand)}\n")

        print("You have:")
        printHand([card[0] for card in pHand], asciiCards)

        print(f"Total of {getTotal(pHand)}\n")
        time.sleep(1)

# Prints the title and rules
print("----------------------------------------------------")
print("                   Baby Blackjack                   ")
print("      You and the dealer will receive 2 cards       ")
print("  Whoever has the bigger number that is <= 21 wins  ")
print("         If you go over 21 the dealer wins          ")
print("         If the dealer goes over 21 you win         ")
print("               Blackjack pays 3 to 2                ")
print("              Dealer must hit soft 17               ")
print("                   Input h to hit                   ")
print("                  Input s to stand                  ")
print("----------------------------------------------------")

# Dictionary for the shuffled deck
shuffledDeck = {}

# Loop to play Blackjack
while True:
    # Shuffle the deck if the deck has 4 or less cards in it
    if len(shuffledDeck) <= 4:
        shuffleDeck(shuffledDeck)

    # Player hand
    playerHand = []

    # Determines if player hit blackjack
    blackjack = False

    # Dealer hand
    dealerHand = []

    # Draws the first 2 cards for the player and dealer
    for i in range(0, 2):
        drawCard(playerHand)

        drawCard(dealerHand)

    # Checks if player and dealer got blackjack before continuing to user choice
    if getTotal(playerHand) == 21 and getTotal(dealerHand) == 21:
        print("\nThe dealer has:")
        printHand([card[0] for card in dealerHand], asciiCards)
        print("You have:")
        printHand([card[0] for card in playerHand], asciiCards)
        print("No one wins. Push.")
        if playAgain():
            continue
        break

    # Checks if player got blackjack before continuing to user choice
    if getTotal(playerHand) == 21:
        print("\nYou have:")
        printHand([card[0] for card in playerHand], asciiCards)
        print("You hit blackjack!")
        blackjack = True

    # Checks if dealer got blackjack before continuing to user choice
    if getTotal(dealerHand) == 21:
        print("\nThe dealer has:")
        printHand([card[0] for card in dealerHand], asciiCards)
        print("You lose.")
        if playAgain():
            continue
        break

    printDetails(dealerHand, playerHand)

    # Loop to play the round of blackjack with user decisions and the dealers turn
    while True:
        if not blackjack:
            choice = input("What do you want to do?: ").lower()
        else:
            choice = "s"

        # If user decides to hit draw a card and check for 21 or bust
        if choice == "h":
            drawCard(playerHand)
            printDetails(dealerHand, playerHand)

            if getTotal(playerHand) > 21:
                print("You busted. You lose.")
                break
            elif getTotal(playerHand) == 21:
                print("The dealer must get 21 to push else you win!")
                blackjack = True

        # If user decides to stand move on to dealers turn
        elif choice == "s":
            printDetails(dealerHand, playerHand, 1)

            # Loop to draw cards for dealer until they arn't allowed to draw any more
            while getTotal(dealerHand) < 17 or (getTotal(dealerHand) == 17 and hasAces(dealerHand)):
                drawCard(dealerHand)
                printDetails(dealerHand, playerHand, 1)

            # Checks for the winner
            if getTotal(dealerHand) > 21:
                print("Dealer busted! You win!\n")
                break

            if getTotal(dealerHand) == getTotal(playerHand):
                print(f"You have {getTotal(playerHand)} and the dealer has {getTotal(dealerHand)}. No one wins. Push.\n")
                break

            if getTotal(dealerHand) > getTotal(playerHand):
                print(f"The dealer has {getTotal(dealerHand)} and you have {getTotal(playerHand)}. Dealer wins.\n")
                break

            print(f"You have {getTotal(playerHand)} and the dealer has {getTotal(dealerHand)}. You win!\n")
            break

        else:
            print("Invalid input! Try again!\n")
            continue

    if not playAgain():
        break

print("\nThanks for playing!")
