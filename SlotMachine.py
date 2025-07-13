# ----slot machine project----
'''
                                        #KEY POINTS
1. for-else, where else statement executes if the break statement in if-block is not executed
2. items() method gives key-value pair from dictionary(key,value)
3. an uderscore _ can be used as anonymous variable for iteration in for loop. used to reduce the number of unused variables. hence saves memory
4. copied_list = org_list[:] --> here [:] is necessary to copy the list for once and make the new copy independent of any changes made to original list thenafter.
                                if it is not added, changes made to current_symbol affects all_symbols and vice-versa
5. enumerate() method gives the index as well as the item from a collection
6. the end parameter specifies what to print at the end of the output, instead of the default newline character (\n) eg:print(column[row], end=" | ")
    by default, when a print statement adds a new line after the output meaning it moves to a next line
7. using print() statement after a loop consisting of print statements with 'end' attribute print every row and then moves to next line
8.  print("You won on lines: ", *winning_lines)
        # here, * is called splat operator or unpack operator that will pass every single line number from winning_lines to print function
9. variables can be inserted into a string using f-string, string concatenation or splat operator.
'''
import random  # generate random values

# global constants here
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {  # dictionary
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}
symbol_value = {  # dictionary
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # for-else, where else statement executes if the break statement in if-block is not executed
            winnings += values[symbol]*bet
            # (line+1) because line is the index and we want output in counting numbers, not starting with 0.
            winning_lines.append(line+1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # list to store symbols

    for symbol, symbol_count in symbols.items():  # key-value pair from dictionary(key,value)
        for _ in range(symbol_count):
            # here, _ is an anonymous variable for iteration. used to reduce the number of unused variables
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copying the all_symbols list.
        # here [:] is necessary to copy the list for once and make the new copy independent of any changes made to original list thenafter
        # if it is not added, changes made to current_symbol affects all_symbols and vice-versa
        # alternatively, copy() method can be used

        for _ in range(rows):
            # using the imported module i.e random
            value = random.choice(all_symbols)
            # remove the first instance of the given value in the list
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        # enumerate gives the index as well as the item. so, i=index and column=item
        for i, column in enumerate(columns):
            # suppose for a list of length 3, the maximum index is 2 (0,1,2) that is equal to ((length_of_list)-1)
            if i != len(columns)-1:
                # print the separator "|" if i(index) is not equal to maximum index in the list
                print(column[row], end=" | ")
            else:
                # for a list of 3, it outputs (1|2|3), where the numbers represent items
                print(column[row], end="")

        print()  # print every row and then goto next line


def deposit():
    amount = input("What would you like to deposit? $")
    while True:
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a valid number.")
    return amount


def get_num_of_lines():
    # string concatenation
    lines = input("Enter the number of lines (1-"+str(MAX_LINES)+"): ")
    while True:
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be in the range (1-{MAX_LINES}).")
        else:
            print("Enter a valid number of line(s).")
    return lines


def get_bet_amt():
    # f-string implementation
    amount = input(
        f"What would you like to bet on each line ${MIN_BET}-${MAX_BET}?: $")
    while True:
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Bet amount must be greater than 0.")
        else:
            print("Enter a valid number.")
    return amount


def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet_amt()
        total_bet = bet*lines
        if total_bet > balance:
            diff = total_bet-balance
            print(
                f"You do not have enough balance! You are ${diff} short for the bet.\nYour current balance is ${balance}.")

            depo_prompt = input(
                "Would you like to topup your account with new deposit?(Y/N): ").strip().upper()  # remove leading and trailing whitespaces and to uppercase
            if depo_prompt == "Y":
                main()
            elif depo_prompt == "N":
                print("Thank you for playing!")
                exit()
            else:
                print("Invalid Input!")
        else:
            break
    print(
        f"You're betting ${bet} on {lines} lines. Total bet amount is: ${total_bet}.")

    # generate slot machine now
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    if len(winning_lines) > 0:
        print(f"Congrats! You won ${winnings}.")

        print("You won on lines: ", *winning_lines)
        # here, * is called splat operator or unpack operator that will pass every single line number from winning_lines to print function
        # suppose winning_lines list has [1,2] then, the output will be as 1 2.
    else:
        print(f"You won ${winnings}.")

    return winnings-total_bet


def main():
    balance = deposit()

    while True:

        print(f"Your current balance is ${balance}.")
        answer = input("Press enter to play (q to quit):")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")


main()
