import random

choiceMap = {  # dict
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "quit"
}


def game(user, computer):
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a DRAW!")
    else:
        match (user, computer):
            case ("rock", "paper"):
                print("You lost!")
            case ("rock", "scissors"):
                print("You won!")

            case ("paper", "rock"):
                print("You won!")
            case ("paper", "scissors"):
                print("You lost!")

            case ("scissors", "rock"):
                print("You lost!")
            case ("scissors", "paper"):
                print("You won!")
            case _:
                print("Invalid Input!")


def main():
    compChoiceList = ["rock", "paper", "scissors"]
    while True:
        try:
            userInput = int(input(
                "Enter 1. rock, 2.paper, 3. scissors or 4 to quit: "))
        except ValueError:  # if not integer
            print("Invalid Input!")
            continue
        if userInput == 4:  # quit
            print("Thank you for playing!")
            break
        if userInput not in choiceMap:
            print("Input out of range (1-4)!")
            continue
        # here, userInput is the key in the dictionary
        user_choice = choiceMap.get(userInput)
        computer_choice = random.choice(compChoiceList)
        game(user_choice, computer_choice)
        print()


main()
