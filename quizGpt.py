"""
Basic Hard-coded quiz
takes answers for given questions as input.
returns correct or incorrect after every question.
returns final score at the end.
"""
a = input("Enter your name: ")
print("Hello,", a+"! Let's start the quiz.")


def quizRMA():
    # create lists with question, options, correctAnswer
    questions = [("Who is the current manager of Real Madrid?/n",
                 ["1. Zinedine Zidane   2. Carlo Ancelotti"], "2"),
                 ("Which stadium is the home of Real Madrid?/n",
                  ["1. Santiago Bernabeu  2. Camp Nou "], "1"),
                 ("What color are Real Madrid's home kits traditionally?/n",
                  ["1. Red   2. White "], "2"),
                 ("Which player is known as \"The Galactico\" for Real Madrid?/n",
                  ["1. Cristiano Ronaldo  2. Sergio Ramos "], "1"),
                 ("What year was Real Madrid founded?/n",
                  ["1. 1902   2. 1920 "], "1")]

    score = 0

    for quest, option, correctAnswer in questions:
        print(quest)
        for opt in option:
            print(opt)
        userAns = input(
            "Choose your answer (1 or 2) or press any alphabet to quit: ")

        if (userAns.isalpha()):
            print("You chose to exit the quiz. Thank you!")
            break
        elif (userAns == correctAnswer):
            print("Congratulations! Your answer is correct.")
            score = score+1
        else:
            print("Sorry, your answer is incorrect.")

    print(
        f"The quiz has ended.\nYour final score is: {score}.\nThank You for playing!")


quizRMA()
