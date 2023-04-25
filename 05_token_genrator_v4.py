"""Component 3 (random tokens) v4
Calculate percentages to ensure the odds favour the house
5% unicorns, 30% donkeys and remaining 65% horses/zebras"""

import random

Starting_balance = 100
balance = Starting_balance

# Testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

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

    # output
    print(f"Starting Balance = ${Starting_balance:.2f}")
    print(f"Final Balance = ${balance:.2f}")
