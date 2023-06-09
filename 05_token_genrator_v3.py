"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 10% chance of unicorn and 30% chance for each of
donkey, zebra, or horse"""

import random

tokens = ["unicorn",
          "horse","horse", "horse",
          "donkey", "donkey", "donkey",
          "zebra", "zebra", "zebra"]
Starting_balance = 100
balance = Starting_balance

# Testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    # output
    print(f"Starting Balance = ${Starting_balance:.2f}")
    print(f"Final Balance = ${balance:.2f}")
