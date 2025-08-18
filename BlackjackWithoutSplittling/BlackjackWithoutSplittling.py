"""Program to play a blackjack without splitting"""

import random
import time
import os

def clear():
    """Function to clear the console"""
    os.system("cls")

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

def moreMoney():
    """Function to buy in more money to bet with"""
    if input("Do you want to buy in more money? y for yes anything else for no?: ").lower() == "y":
        while True:
            try:
                return int(input("How much: "))
            except ValueError:
                print("Invalid input. Enter a number!")
    else:
        return 0

def hit(pHand):
    """Function to hit"""
    drawCard(pHand)

    clear()
    printTitleRules()

    printDetails(dealerHand, pHand)

    if getTotal(pHand) > 21:
        print("You busted. You lose.\n")
        print(f"You lost your bet of ${bet:,}\n")
        return "break"

    if getTotal(playerHand) == 21:
        print("The dealer must get 21 to push else you win!")
        return "acsTrue"

    return "allGood"

def printTitleRules():
    """Function to print the title and the rules of the game"""
    print("----------------------------------------------------")
    print("                     Blackjack                      ")
    print("      You and the dealer will receive 2 cards       ")
    print()
    print("   You can choose to hit, stand, split, or double   ")
    print()
    print("         When you are done the dealer plays         ")
    print()
    print("             Hit gives you another card             ")
    print()
    print(" Stand stops your turn and moves onto dealers turn  ")
    print()
    print("  Double gives you one card before moving onto the  ")
    print("  dealers turn. When you double you have to double  ")
    print("  your original bet. You can also only double with  ")
    print(" your first 2 cards, so if you hit you cant double  ")
    print()
    print("  Whoever has the bigger number that is <= 21 wins  ")
    print()
    print("         If you go over 21 the dealer wins          ")
    print()
    print("         If the dealer goes over 21 you win         ")
    print()
    print("               Blackjack pays 3 to 2                ")
    print()
    print("              Dealer must hit soft 17               ")
    print()
    print("  If you run out of money you will be asked if you  ")
    print("           want to buy in for more money            ")
    print()
    print("                   Input h to hit                   ")
    print("                  Input s to stand                  ")
    print("                 Input d to double                  ")
    print("----------------------------------------------------")

printTitleRules()

# Dictionary for the shuffled deck
shuffledDeck = {}

while True:
    try:
        money = int(input("\nHow much do you want to buy in?: "))
        break
    except ValueError:
        print("Invalid input! Enter a number")

# Loop to play Blackjack
while True:
    print(f"\nCurrent money: ${money:,}\n")
    # Shuffle the deck if the deck has 4 or less cards in it
    if len(shuffledDeck) <= 4:
        shuffleDeck(shuffledDeck)

    # Player hands
    playerHand = []
    playerHands = [playerHand]

    # Determines if player hit natural blackjack
    naturalBlackjack = False

    # True if you have no money and chose to not buy in for more
    # Breaks out of the main loop
    noMoreMoney = False

    # Dealer hand
    dealerHand = []

    # Loop to get bet and ensure it is valid input as well as not too large
    while True:
        # Makes sure a number is entered
        try:
            # Makes sure bet isn't larger then money
            while True:
                # Asks to re buy in if you run out of money
                # If you choose not to buy in end the game
                if money == 0:
                    money += moreMoney()
                    if money == 0:
                        noMoreMoney = True
                        break

                bet = int(input("\nEnter your bet: "))
                if bet > money:
                    print("\nBet larger than your amount of money.")
                    continue

                money -= bet
                break
            break
        except ValueError:
            print("\nInvalid input! Please enter a number.")

    if noMoreMoney:
        break

    # Draws the first 2 cards for the player and dealer
    for i in range(0, 2):
        drawCard(playerHand)

        drawCard(dealerHand)

    # Checks if player and dealer got blackjack before continuing to user choice
    # Push returns bet
    if getTotal(playerHand) == 21 and getTotal(dealerHand) == 21:
        print("\nThe dealer has:")
        printHand([card[0] for card in dealerHand], asciiCards)

        print("You have:")
        printHand([card[0] for card in playerHand], asciiCards)

        print("No one wins. Push.")
        print(f"You get back your bet of ${bet:,}")

        money += bet

        if playAgain():
            clear()
            printTitleRules()
            continue
        break

    # Checks if player got blackjack before continuing to user choice
    if getTotal(playerHand) == 21:
        print("\nYou have:")
        printHand([card[0] for card in playerHand], asciiCards)

        print("You hit blackjack!")

        naturalBlackjack = True

    # Checks if dealer got blackjack before continuing to user choice
    if getTotal(dealerHand) == 21:
        print("\nThe dealer has:")
        printHand([card[0] for card in dealerHand], asciiCards)

        print("You lose.\n")
        print(f"You lost your bet of ${bet:,}\n")

        if playAgain():
            clear()
            printTitleRules()
            continue
        break

    printDetails(dealerHand, playerHand)

    # Used to auto choose stand once you hit 21 from hitting or when you double
    autoChooseStand = False

    # Tracks if you have hit already baring you from doubling or splitting
    hasHit = False

    # Loop to play the round of blackjack with user decisions and the dealers turn
    while True:
        if naturalBlackjack or autoChooseStand:
            choice = "s"
        else:
            choice = input("What do you want to do?: ").lower()

        # If user decides to hit draw a card and check for 21 or bust
        if choice == "h":
            resultHit = hit(playerHand)

            if resultHit == "break":
                break

            if resultHit == "acsTrue":
                autoChooseStand = True

            hasHit = True

        # If user decides to double draw one more card and double the bet amount
        elif choice == "d":
            if hasHit:
                print("\nYou have already hit this turn, you can't double. Pick another option.\n")
                continue

            if bet > money:
                print("\nYou don't have enough money to double. Pick another option.\n")
                continue

            money -= bet
            bet *= 2

            drawCard(playerHand)

            clear()
            printTitleRules()

            printDetails(dealerHand, playerHand)

            print(f"Your new bet is ${bet:,}")

            autoChooseStand = True

        # If user decides to stand move on to dealers turn
        elif choice == "s":
            clear()
            printTitleRules()

            printDetails(dealerHand, playerHand, 1)

            # Loop to draw cards for dealer until they arn't allowed to draw any more
            while getTotal(dealerHand) < 17 or (getTotal(dealerHand) == 17 and hasAces(dealerHand)):
                drawCard(dealerHand)

                clear()
                printTitleRules()

                printDetails(dealerHand, playerHand, 1)

            # Checks for dealer bust
            if getTotal(dealerHand) > 21:
                print("Dealer busted! You win!\n")

                if naturalBlackjack:
                    money += bet + bet * 1.5
                    print(f"Since you got natural blackjack you won ${bet * 1.5:,}", end = " ")
                    print(f"plus your original bet of ${bet:,}", end = " ")
                    print(f"for a total of ${bet + bet * 1.5:,}!\n")
                else:
                    money += bet * 2
                    print(f"You won ${bet:,} plus your original bet of ${bet:,}", end = " ")
                    print(f"for a total of ${bet * 2:,}\n")

                break

            # Checks for push
            if getTotal(dealerHand) == getTotal(playerHand):
                print(f"You have {getTotal(playerHand)} and the dealer has",end = " ")
                print(f"{getTotal(dealerHand)}. No one wins. Push.\n")

                money += bet
                print(f"You get your back your bet of ${bet:,}\n")

                break

            # Checks for dealer win
            if getTotal(dealerHand) > getTotal(playerHand):
                print(f"The dealer has {getTotal(dealerHand)} and you have", end = " ")
                print(f"{getTotal(playerHand)}. Dealer wins.\n")
                print(f"You lost your bet of ${bet:,}\n")
                break

            # Checks for player win
            print(f"You have {getTotal(playerHand)} and the dealer has", end = " ")
            print(f"{getTotal(dealerHand)}. You win!\n")

            if naturalBlackjack:
                money += bet + (bet * 1.5)
                print(f"Since you got natural blackjack you won ${bet * 1.5:,}", end = " ")
                print(f"plus your original bet of ${bet:,}", end = " ")
                print(f"for a total of ${bet + bet * 1.5:,}!\n")
            else:
                money += bet * 2
                print(f"You won ${bet:,} plus your original bet of ${bet:,}", end = " ")
                print(f"for a total of ${bet * 2:,}\n")

            break

        else:
            print("Invalid input! Try again!\n")
            continue

    if not playAgain():
        break

    clear()
    printTitleRules()

print("\nThanks for playing!")
