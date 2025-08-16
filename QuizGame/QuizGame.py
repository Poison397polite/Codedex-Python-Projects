"""Simple Quiz Game"""

import random

# Open the file Questions.txt and makes each line the value
# and the line number the key for the questions dictionary.
with open("Questions.txt", "r", encoding = "utf8") as file:
    questions = file.readlines() # Reads the file Questions.txt and makes every line a value in list

    questions = [line.strip() for line in questions] # Removes the \n in every line

# Open the file Answers.txt  and make each line the value
# and the line number the key for the answers dictionary.
with open("Answers.txt", "r", encoding = "utf8") as file:
    answers = file.readlines() # Reads the file Answers.txt and makes every line a value in list

    answers = [line.strip() for line in answers] # Removes the \n in every line

# Keep track of user score for all 50 questions
totalScore = 0

# Main loop keeping the user playing until they want to stop or no more questions
while True:
    # Gets 10 different numbers between 0 and the current length of the questions list
    # for use as indexes to get questions and answers
    randomQuestions = random.sample(range(0, len(questions)), 10)
    # Keeps track of user score for the current 10 questions
    score = 0

    # Loop to ask all the questions and determine if it was answered correctly
    for question in randomQuestions:
        print(f"{questions[question]}\n")
        answer = input("Answer: ").lower()

        # If the question was answered correctly increment score by 1
        if answer == answers[question].lower():
            print("\nCorrect!\n")
            score += 1
        # If the question was answered incorrectly print the correct answer for the user
        else:
            print("\nIncorrect!")
            print(f"The answer was {answers[question]}\n")

    # Removes questions already asked
    for question in sorted(randomQuestions, reverse = True):
        answers.pop(question)
        questions.pop(question)

    print(f"You got {score} / 10")

    totalScore += score

    if len(questions) < 10:
        print("There are no more questions")
        break

    if input("Do you want to keep playing? y for yes anything else for no: ").lower() != "y":
        break

print(f"You got {totalScore} / 50")
print("Thanks for playing!")
