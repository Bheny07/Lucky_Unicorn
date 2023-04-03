""" Yes/No checking function
based on 01_yes_n0_v3
"""


# Functions go here...
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


# Main routine


show_instructions = yes_no("Have you played this game before?: ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun?: ")
print(f"You entered '{having_fun}'")


