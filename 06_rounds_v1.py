"""Component 4 (game mechanics and looping) v4
Based on 05_token_generator_v4 but hard-wired to only allocate donkeys
 Gives user feedback about number of rounds and maintains balance.
 Test amount set to $5"""

import random

# main routine
test_amount = 5
balance = test_amount

rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(6, 36)  # can only be a donkey

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

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


