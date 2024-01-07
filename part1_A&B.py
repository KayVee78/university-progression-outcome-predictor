# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1998488

# Date: 2023-04-21

import sys

pass_credits = 0
defer_credits = 0
fail_credits = 0
total_credits = 0


def validate_user_input():
    global pass_credits, defer_credits, fail_credits
    try:
        pass_credits = int(input('Please enter your credit at pass\t: '))
    except ValueError:
        print('Integer required')
        sys.exit()
    if pass_credits not in range (0,121,20): # (start, stop, step)
        print('Out of range')
        sys.exit()

    try:
        defer_credits = int(input('Please enter your credit at defer\t: '))
    except ValueError:
        print('Integer required')
        sys.exit()
    if defer_credits not in range (0,121,20): # (start, stop, step)
        print('Out of range')
        sys.exit()

    try:
        fail_credits = int(input('Please enter your credit at fail\t: '))
    except ValueError:
        print('Integer required')
        sys.exit()
    if fail_credits not in range (0,121,20): # (start, stop, step)
        print('Out of range')
        sys.exit()


def progression_outcome(passs, defer, fail):
    if (passs+defer+fail) != 120:
        print('Total incorrect')
        sys.exit()
    if passs == 120 :
        print('Progression Outcome : Progress')
    elif passs == 100 and (defer == 0 or fail == 0):
        print('Progression Outcome : Progress(module trailer)')
    elif passs <= 80 and (defer >= 40 or fail <= 60):
        print('Progression Outcome : Do not progress – module retriever')
    elif fail >= 80:
        print('Progression Outcome : Exclude')


def main():
    validate_user_input()
    progression_outcome(pass_credits, defer_credits, fail_credits)


main()