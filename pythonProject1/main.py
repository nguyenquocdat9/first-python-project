import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(collumns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = collumns[0][line]
        for col in collumns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, number_of_symbol in symbols.items():
        for i in range(number_of_symbol):
            all_symbols.append(symbol)
    collumns = []
    for col in range(cols):
        collumn = []
        current_symbols = all_symbols.copy()  # [:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            collumn.append(value)
        collumns.append(collumn)
    return collumns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print(end="\n")


def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isnumeric():
            amount = int(amount)
            if amount <= 0:
                print("Amount must be positive")
            else:
                break
        else:
            print("Amount must be a number")
    return amount


def get_number_of_lines():
    while True:
        line = input("Enter number of lines to bet on "
                     "(1 - " + str(MAX_LINE) + "): ")
        if line.isnumeric():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print("Line must be between 1 and "
                      + str(MAX_LINE))
        else:
            print("Line must be a number")
    return line


def get_bet():
    while True:
        amount = input("Enter amount to bet on each line: ")
        if amount.isnumeric():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between "
                      + str(MIN_BET) + " and " + str(MAX_BET))
        else:
            print("Amount must be a number")
    return amount


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount,"
                  f" your current balance is {balance}")
        else:
            print(f"You are betting {bet} on {lines} lines."
                  f" Total bet is equal to {total_bet}")
            break
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"you won {winnings}")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        answer = input("do you want to play? (y/n): ")
        if answer == "n":
            break
        balance += game(balance)
    print(f"you left the game with {balance}")


if __name__ == "__main__":
    main()
