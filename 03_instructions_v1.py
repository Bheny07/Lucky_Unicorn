""" Took function from component 03_v1 as the basis for this new function which
incorporates both yes/no and shows instructions"""


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
    print("Program continues")
    print()


# Main Routine
played_before = yes_no("Have you played this game before?: ")

if played_before == "no":
    instructions()
else:
    print("Program continues")