import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Slot machine
ROWS = 3
COLS = 3

symbol_count = {
    "!": 2,
    "@": 4,
    "#": 6,
    "$": 8,
    "%": 2,
    "^": 2,
}

rewards = {
    ("!", "!", "!"): 100,
    ("@", "@", "@"): 200,
    ("#", "#", "#"): 300,
    ("$", "$", "$"): 400,
    ("%", "%", "%"): 500,
    ("^", "^", "^"): 600,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to play on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line? (${MIN_BET}-{MAX_BET}) ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet


def calculate_reward(spin, bet):
    reward = 0
    for combination, value in rewards.items():
        if spin[0][0] == spin[1][0] == spin[2][0] == combination[0] or \
           spin[0][1] == spin[1][1] == spin[2][1] == combination[1] or \
           spin[0][2] == spin[1][2] == spin[2][2] == combination[2] or \
           spin[0][0] == spin[1][1] == spin[2][2] == combination[0] or \
           spin[0][2] == spin[1][1] == spin[2][0] == combination[2]:
            reward += value * bet
    return reward


def main():
    print("Welcome to the Slot Machine Game!")
    balance = deposit()

    while True:
        lines = get_number_of_lines()
        bet = get_bet()

        total_spins = 0
        while True:
            total_spins += 1
            total_bet = bet * lines

            if total_bet > balance:
                print(f"You don't have enough money in your balance to cover your bet. Balance: ${balance}")
                break

            balance -= total_bet
            print(f"\n--- Spin #{total_spins} ---")
            print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to ${total_bet}")

            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)

            reward = calculate_reward(slots, bet)
            if reward > 0:
                print(f"Congratulations! You won ${reward}.")
                balance += reward
            else:
                print("Better luck next time!")

            print(f"Current balance: ${balance}")

            if total_spins >= 5:
                play_again = input("Do you want to play again? (y/n) ").lower()
                if play_again != "y":
                    break
            else:
                print(f"\n--- Spin #{total_spins + 1} ---")

    print(f"Thank you for playing! Your remaining balance is ${balance}.")
    withdraw = input("Do you want to withdraw your balance? (y/n) ").lower()
    if withdraw == "y":
        print(f"Withdrawn ${balance}. Goodbye!")
        balance = 0
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
