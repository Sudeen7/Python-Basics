"""
computer generates random number using random module, user guesses a number (input).
the numbers are compared, returns 'too high' if (input-computer)>20, else returns 'too low', returns 'very close' if (input-computer)<5
"""
import random

# assign minimum and maximum value for range
min, max = 1, 50


def game(user, comp):

    if user == comp:
        print("----Congratulations! Your guess was correct.----")

    elif abs(user-comp) > 20:  # abs gives absolute value (i.e. positive magnitude)
        print("----Your guess was TOO HIGH!----") if user > comp else print(
            "----Your guess was TOO LOW!----")

    elif abs(user-comp) < 5:
        print("----Your guess was VERY CLOSE!----")
    else:
        print("----Incorrect Guess!----")
    print(f"You guessed: {user} \nComputer Generated: {comp}")


def main():

    while True:
        consent = input(
            f"Enter number in range ({min}-{max}) to play or 'Q' to quit: ").strip().upper()
        if consent == "Q":
            print("----Thank you for playing!----")
            break
        else:
            try:
                numConsent = int(consent)
                condition = min <= numConsent <= max
                if condition:
                    comp = random.randint(min, max)
                    game(numConsent, comp)
                if not condition:
                    print("Input out of range!")
            except ValueError:
                print("Invalid Input! Enter a valid integer inside specified range.")


main()
