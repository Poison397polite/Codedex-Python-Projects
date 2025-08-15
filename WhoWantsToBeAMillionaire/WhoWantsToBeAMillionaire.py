"""Program to play Who wants to be a millionaire"""

import random

questions = {} # Dictionary of all the questions in the game
# Fills the questions dictionary with the questions in Questions.txt
# Each line number is the key and each lines text is the value
with open("Questions.txt", "r", encoding = "utf8") as file:
    for i, line in enumerate(file, start = 1):
        questions[i] = line.strip() # strip() removes \n

correctAnswers = {} # Dictionary of all the correct answers
# Fills the correctAnswers dictionary with the correct answers from CorrectAnswers.txt
# Each line number is the key and each lines text is the value
with open("CorrectAnswers.txt", "r", encoding = "utf8") as file:
    for i, line in enumerate(file, start = 1):
        correctAnswers[i] = line.strip() # strip() removes \n

incorrectAnswers = {} # Dictionary of all the incorrect answers
# Opens IncorrectAnswers.txt and stores every line in a list without the \n
with open("IncorrectAnswers.txt", "r", encoding = "utf8") as file:
    lines = [line.strip() for line in file] # remove \n

# Loops through all the lines and fills the incorrectAnswers dictionary with a key from 1 to 15
# and the value is a list of 3 lines each
for i in range(0, len(lines), 3):
    key = i // 3 + 1 # 1, 2, 3...
    incorrectAnswers[key] = lines[i : i + 3]

questionCash = {} # Dictionary for all the amounts of cash for questions
 # Fills the questionCash dictionary with the numbers in QuestionCash.txt converted to an integer
 # Each line number is the key
with open("QuestionCash.txt", "r", encoding = "utf8") as file:
    for i, line in enumerate(file, start = 1):
        questionCash[i] = int(line.strip()) # strip removes \n, int() converts to integer

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

def lifeline5050():
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

def lifelineAskTheAudience():
    """Function to execute the Ask the Audience lifeline"""
    # Gets input from the "audience" favored in the correct answer but can be wrong
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
    # "Calls" a "friend" and gets an answer from them that is correct 4 out of 5 times
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

    # Used to verify if a lifelife has already been used on the current question
    usedLifeline = False

    # Loop ensureing valid input as well as working with lifelines
    while True:
        answer = input("\nYour answer: ")

        # Checks input to ensure the input was valid
        if answer.lower() not in ("a", "b", "c", "d", "lifeline"):
            print("\nInvalid input try again!")

        # Displays available lifelines and applies the lifeline chosen
        elif answer.lower() == "lifeline":
            print()
            # Checks if a lifeline has been used this question
            # or if no lifelines are remaining before proceeding to lifelines
            if usedLifeline:
                print("You already used a lifeline this question.")
            elif len(lifelines) < 1:
                print("You have no more lifelines!")
            else:
                # Prints available lifelines
                for lifeline in lifelines:
                    print(f"{lifeline}")

                chosenLifeline = input("\nChose what lifeline you want to use: ")
                chosenLifeline = chosenLifeline.lower()
                print()

                # Calls the lifeline5050 function and toggles usedLifeline to true
                if "50" in chosenLifeline and lifelines[0] == "50 / 50":
                    lifeline5050()
                    usedLifeline = True

                # Calls the lifelineAskTheAudience function and toggles usedLifeline to true
                elif "ask" in chosenLifeline and any("ask" in x.lower() for x in lifelines):
                    lifelineAskTheAudience()
                    usedLifeline = True

                # Calls the lifelinePhoneAFriend function and toggles usedLifeline to true
                elif "phone" in chosenLifeline and any("phone" in x.lower() for x in lifelines):
                    lifelinePhoneAFriend()
                    usedLifeline = True

                # Only activates if you entered an already used or non existant lifeline
                else:
                    print("Invalid input")
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
    if i in (5, 10):
        print(f"You just locked in ${questionCash[i]:,}, you are now guaranteed that money!\n")
    elif i == 15:
        print("You are now a millionaire!")

if i > 10 < 15:
    print("\nYou didn't make a million but you are going home with $32,000")
elif i > 5 < 10:
    print("\nYou didn't make a million but you are going home with $1,000")

print("\nThanks for playing!")
