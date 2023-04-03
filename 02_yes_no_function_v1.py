""" Yes/No checking function
based on 01_yes_n0_v3
"""

show_instructions = ""
while show_instructions != "x":

    # Ask user if they have played before
    show_instructions = input("Have you played this game before?: ").lower()

    # If they say yes, output 'Program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output 'Display Instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display Instructions")

    # Otherwise - show error
    else:
        print("Please answer 'yes or 'no'")

    print(f"You Entered '{show_instructions}'")