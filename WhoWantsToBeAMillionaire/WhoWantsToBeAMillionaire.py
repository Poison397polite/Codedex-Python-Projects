"""Program to play Who wants to be a millionaire"""

import random

questions = { # Dictionary for all the questions in the game
    1: "The Earth is approximately how many miles away from the Sun?",
    2: "Which insect shorted out an early supercomputer and inspired the term \"computer bug\"?",
    3: "Which of the following men does not have a chemical element named for him?",
    4: "Which of the following landlocked countries is entirely contained within another country?",
    5: "In the children's book series, where is Paddington Bear originally from?",
    6: "Who is credited with inventing the first mass-produced helicopter?",
    7: "What letter must appear at the beginning of the registration number of all non-military aircraft in the U.S.?",
    8: "During WWII, U.S. soldiers used the first commercial aerosol cans to hold what?",
    9: "The U.S. icon \"Uncle Sam\" was based on Samuel Wilson, who worked during the War of 1812 as a what?",
    10: "Who did artist Grant Wood use as the model for the farmer in his classic painting \"American Gothic\"?",
    11: "For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled \"coffee,\" \"tea,\" \"Coke\" and what?",
    12: "According to the Population Reference Bureau, what is the approximate number of people who have ever lived on earth?",
    13: "In addition to his career as an astrologer and \"prophet,\" Nostradamus published a 1555 treatise that included a section on what?",
    14: "Although he and his wife never touched a light switch for fear of being shocked, who was the first president to have electricity in the White House?",
    15: "Which of these U.S. presidents appeared on the television series 'Laugh-In'?"
}

correctAnswers = { # Dictionary of all the correct answers
    1: "93 million",
    2: "Moth",
    3: "Isaac Newton",
    4: "Lesotho",
    5: "Peru",
    6: "Igor Sikorsky",
    7: "N",
    8: "Insecticide",
    9: "Meat inspector",
    10: "His dentist",
    11: "Fresca",
    12: "100 billion",
    13: "Making jams and jellies",
    14: "Benjamin Harrison",
    15: "Richard Nixon"
}

incorrectAnswers = { # Dictionary for all the incorrect answers
    1: ["9.3 million", "39 million", "193 million"],
    2: ["Roach", "Fly", "Japanese beetle"],
    3: ["Albert Einstein", "Niels Bohr", "Enrico Fermi"],
    4: ["Burkina Faso", "Mongolia", "Luxembourg"],
    5: ["India", "Canada", "Iceland"],
    6: ["Elmer Sparry", "Ferdinand von Zeppelin", "Gottlieb Daimler"],
    7: ["A", "U", "L"],
    8: ["Cleaning fluid", "Antiseptic", "Shaving cream"],
    9: ["Mail deliverer", "Historian", "Weapons mechanic"],
    10: ["Traveling salesman", "Local sheriff", "His butcher"],
    11: ["V8", "Yoo-hoo", "A&W"],
    12: ["50 billion", "1 trillion", "5 trillion"],
    13: ["Training parrots to talk", "Cheating at card games", "Digging graves"],
    14: ["Ulysses S. Grant", "Chester A. Arthur", "Andrew Johnson"],
    15: ["Lyndon Johnson", "Jimmy Carter", "Gerald Ford"]
}

questionCash = { # Dictionary for all the amounts of cash for questions
    1: 100,
    2: 200,
    3: 300,
    4: 500,
    5: 1000,
    6: 2000,
    7: 4000,
    8: 8000,
    9: 16000,
    10: 32000,
    11: 64000,
    12: 125000,
    13: 250000,
    14: 500000,
    15: 1000000
}

lifelines = [ # A list of the available lifelines, they get removed when used
    "50 / 50",
    "Ask the Audience",
    "Phone a Friend"
]

def printQuestionAndAnswers():
    """Function that will print the questions and answers"""
    print(f"Question {i} for ${questionCash[i]:,}:")
    if i in (2, 4, 6, 7, 9, 11):
        print(questions[i])
        print(f"a) {correctAnswers[i]}")
        print(f"b) {incorrectAnswers[i][0]}")
        print(f"c) {incorrectAnswers[i][1]}")
        print(f"d) {incorrectAnswers[i][2]}")
    elif i in (5, 12, 14, 15):
        print(questions[i])
        print(f"a) {incorrectAnswers[i][0]}")
        print(f"b) {correctAnswers[i]}")
        print(f"c) {incorrectAnswers[i][1]}")
        print(f"d) {incorrectAnswers[i][2]}")
    elif i in (1, 3, 8, 10):
        print(questions[i])
        print(f"a) {incorrectAnswers[i][0]}")
        print(f"b) {incorrectAnswers[i][1]}")
        print(f"c) {correctAnswers[i]}")
        print(f"d) {incorrectAnswers[i][2]}")
    else:
        print(questions[i])
        print(f"a) {incorrectAnswers[i][0]}")
        print(f"b) {incorrectAnswers[i][1]}")
        print(f"c) {incorrectAnswers[i][2]}")
        print(f"d) {correctAnswers[i]}")

def lifeline50():
    """Function to execute the 50 / 50 lifeline"""
    # Prints the question again and the answers with 2 incorrect answers removed
    if i in (2, 4, 6, 7, 9, 11):
        print(questions[i])
        print(f"a) {correctAnswers[i]}")
        print(f"d) {incorrectAnswers[i][2]}")
    elif i in (5, 12, 14, 15):
        print(questions[i])
        print(f"a) {incorrectAnswers[i][0]}")
        print(f"b) {correctAnswers[i]}")
    elif i in (1, 3, 8, 10):
        print(questions[i])
        print(f"c) {correctAnswers[i]}")
        print(f"d) {incorrectAnswers[i][2]}")
    else:
        print(questions[i])
        print(f"b) {incorrectAnswers[i][1]}")
        print(f"d) {correctAnswers[i]}")

    # Removes used lifeline from the list so it can only be used once
    lifelines.remove("50 / 50")

def lifelineAsk():
    """Function to execute the Ask the Audience lifeline"""
    audienceAnswer = []
    for i2 in range(1, 1000):
        if i2 % 35 == 0:
            if i in (2, 4, 6, 7, 9, 11):
                audienceAnswer.append(1)
            elif i in (5, 12, 14, 15):
                audienceAnswer.append(2)
            elif i in (1, 3, 8, 10):
                audienceAnswer.append(3)
            else:
                audienceAnswer.append(4)
        else:
            audienceAnswer.append(random.randint(1, 4))

    if round(sum(audienceAnswer) / len(audienceAnswer)) == 1:
        print("The audience thinks the answer is a.\n")
    elif round(sum(audienceAnswer) / len(audienceAnswer)) == 2:
        print("The audience thinks the answer is b.\n")
    elif round(sum(audienceAnswer) / len(audienceAnswer)) == 3:
        print("The audience thinks the answer is c.\n")
    elif round(sum(audienceAnswer) / len(audienceAnswer)) == 4:
        print("The audience thinks the answer is d.\n")

    # Removes used lifeline from the list so it can only be used once
    lifelines.remove("Ask the Audience")

    # Prints the questions and the answer choices
    printQuestionAndAnswers()

def lifelinePhoneAFriend():
    """Function to execute the Phone a Friend lifeline"""
    friendAnswer = random.randint(1, 5)
    if friendAnswer in (1, 2, 3, 4):
        if i in (2, 4, 6, 7, 9, 11):
            print("Your friend thinks the answer is a.\n")
        elif i in (5, 12, 14, 15):
            print("Your friend thinks the answer is b.\n")
        elif i in (1, 3, 8, 10):
            print("Your friend thinks the answer is c.\n")
        else:
            print("Your friend thinks the answer is d.\n")
    else:
        if i in (2, 4, 6, 7, 9, 11):
            print("Your friend thinks the answer is b.\n")
        elif i in (5, 12, 14, 15):
            print("Your friend thinks the answer is c.\n")
        elif i in (1, 3, 8, 10):
            print("Your friend thinks the answer is d.\n")
        else:
            print("Your friend thinks the answer is a.\n")

    # Removes used lifeline from the list so it can only be used once
    lifelines.remove("Phone a Friend")

    # Prints the questions and the answer choices
    printQuestionAndAnswers()

# Prints the title
print("----------------------------------------------------")
print("            Who Want To Be A Millionaire            ")
print("                                                    ")
print(" Answer all 15 questions to win one million dollars ")
print("After every 5 questions you lock in guarenteed money")
print("                                                    ")
print("When you answer question 5 and 10 correctly you will")
print("   lock in a certain amount of money that you are   ")
print("              guaranteed to take home!              ")
print("                                                    ")
print("             You will have 3 lifelines              ")
print("                      50 / 50                       ")
print("This will remove 2 wrong answers making it a 50 / 50")
print("                  Ask the Audience                  ")
print("The audience answers the question and you are showed")
print("           what they think the answer is.           ")
print("                   Phone a Friend                   ")
print(" This will allow you to call a friend and ask them  ")
print("           what they think the answer is.           ")
print("   You can only use your lifelines one time each    ")
print("  Just enter \"lifeline\" when you want to use one  ")
print("                                                    ")
print("           Do you wanna be a millionaire?           ")
print("----------------------------------------------------")

# Loop to ask all questions with correct answer in the correct spots and get input
for i in range(1, 16):
    # Prints the questions and the answer choices
    printQuestionAndAnswers()

    usedLifeline = False # Used to verify if a lifelife has already been used on the current question

    while True: # Loop ensureing valid input as well as working with lifelines
        answer = input("\nYour answer: ")
        # Checks input to ensure the input was valid
        if answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d" and answer.lower() != "lifeline":
            print("\nInvalid input try again!")
        # Displays available lifelines and applies the lifeline chosen
        elif answer.lower() == "lifeline":
            print()
            if usedLifeline:
                print("You already used a lifeline this question.")
            else:
                usedLifeline = True

                for lifeline in lifelines:
                    print(f"{lifeline}")

                chosenLifeline = input("\nChose what lifeline you want to use: ")
                print()

                # Removes 2 incorrect answers for the 50 / 50 lifeline
                if "50" in chosenLifeline and lifelines[0] == "50 / 50":
                    lifeline50()

                # Gets a bunch of random numbers in favor of the correct answer for the Ask the Audience lifeline
                elif "ask" in chosenLifeline.lower() and "ask" in lifelines[0].lower() or "ask" in chosenLifeline.lower() and "ask" in lifelines[1].lower():
                    lifelineAsk()

                # Has a "friend" answer the question giving the correct answer 4 / 5 times
                elif "phone" in chosenLifeline.lower() and "phone" in lifelines[0].lower() or "phone" in chosenLifeline.lower() and "phone" in lifelines[1].lower() or "phone" in chosenLifeline.lower() and "phone" in lifelines[2].lower():
                    lifelinePhoneAFriend()
        else:
            break

    # Checks if the answer input was correct or incorrect
    if (i in (2, 4, 6, 7, 9, 11)) and answer.lower() == "a":
        print(f"\nCorrect! You just won ${questionCash[i]:,}!\n")
    elif (i in (5, 12, 14, 15)) and answer.lower() == "b":
        print(f"\nCorrect! You just won ${questionCash[i]:,}!\n")
    elif (i in (1, 3, 8, 10)) and answer.lower() == "c":
        print(f"\nCorrect! You just won ${questionCash[i]:,}!\n")
    elif (i == 13) and answer.lower() == "d":
        print(f"\nCorrect! You just won ${questionCash[i]:,}!\n")
    else:
        print("\nSorry that is incorrect.")
        break

    # Letting user know when they hit the safe havens and final message
    if i == 5 or i == 10:
        print(f"You just locked in ${questionCash[i]:,}, you are now guaranteed that money!\n")
    elif i == 15:
        print("You are now a millionaire!")

print("\nThanks for playing!")
