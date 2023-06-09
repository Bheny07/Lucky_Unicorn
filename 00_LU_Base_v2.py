""" LU base component -  based on 00_LU_base_v1
Components added after they have been created and tested."""
import random


# Yes/No checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have already played before
        answer = input(question_text).lower()

        # If they say yes, output "Program Continues"
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no output "Display Instructions"
        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        # Otherwise - "Show Error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The Rules of The Game will Go Here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(6, 100)  # can only be a donkey

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # in all other cases the token must be a horse or zebra
        # (subtract $0.5 from balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "Zebra"
                balance -= 0.5

            # otherwise, set the token to horse
            else:
                token = "horse"
                balance -= .5

        # output
        print(f"Round {rounds_played}. Token: {token} Balance ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round\n<enter>"
                               "to play again or 'X' to exit").lower()
        print()
    return balance
    # Main routine


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
played_before = yes_no("Have you played this game before?: ")

if played_before == "no":
    instructions()


# Ask user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

# Main routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"You leave with ${closing_balance:.2f}")
print(formatter("*", "Goodbye"))
