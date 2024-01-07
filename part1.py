# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1998488

# Date: 2023-04-21


# variable declaration
pass_credits = 0
defer_credits = 0
fail_credits = 0
total_credits = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
total_std = 0


def progression_outcome(passs, defer, fail):  # function which determines progression
    # making the declared variables global, to use them throughout the program
    global pass_credits, defer_credits, fail_credits, total_credits, progress_count, trailer_count, retriever_count, \
        exclude_count, total_std

    # implementing a while loop to break soon after the progression outcome is printed &
    # this also increments the specific counter
    while True:
        if (passs+defer+fail) != 120:
            print('Total incorrect')
            break  # break loop -> if total is incorrect

        elif passs == 120:
            print('Progress')
            progress_count += 1
        elif passs == 100 and (defer == 0 or fail == 0):
            print('Progress(module trailer)')
            trailer_count += 1
        elif passs <= 80 and (defer >= 40 or fail <= 60):
            print('Module retriever')
            retriever_count += 1
        elif fail >= 80:
            print('Exclude')
            exclude_count += 1

        total_std += 1
        break


def validate_user_input():
    global pass_credits, defer_credits, fail_credits
    while True:
        try:
            pass_credits = int(input('Please enter your credit at pass\t: '))
        except ValueError:
            print('Integer required')
            continue
        if pass_credits not in range(0, 121, 20):  # (start, stop, step)
            print('Out of range')
            continue

        try:
            defer_credits = int(input('Please enter your credit at defer\t: '))
        except ValueError:
            print('Integer required')
            continue
        if defer_credits not in range(0, 121, 20):  # (start, stop, step)
            print('Out of range')
            continue

        try:
            fail_credits = int(input('Please enter your credit at fail\t: '))
        except ValueError:
            print('Integer required')
            continue
        if fail_credits not in range(0, 121, 20):  # (start, stop, step)
            print('Out of range')
            continue

        # calling progression_outcome function to get the relevant outcome according to the credits inserted
        progression_outcome(pass_credits, defer_credits, fail_credits)

        print()
        # asking the user whether he wants to continue or exit
        print('Would you like to enter another set of data?')
        # Declaring a variable for values 'y' and 'q' to decide the program continuation
        proceeding_char = ""
        # until the user doesn't input 'y' or 'q', program will prompt to ask 'y' or 'q' again and again
        while proceeding_char != 'y' and proceeding_char != 'q':
            proceeding_char = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print()

        # if proceeding_char is 'q' display the histogram and terminate the program
        if proceeding_char == 'q':
            print('-------------------------------------------------------------------------')
            print('Histogram')
            print("Progress", progress_count, "\t: ", (progress_count * '*'))
            print("Trailer", trailer_count, "\t: ", (trailer_count * '*'))
            print("Retriever", retriever_count, ": ", (retriever_count * '*'))
            print("Excluded", exclude_count, "\t: ", (exclude_count * '*'))
            print()
            if total_std == 1:
                print('1 outcomes in total')
            else:
                print(total_std, ' outcomes in total.')
            print('-------------------------------------------------------------------------')
            break

        if proceeding_char == 'y':
            continue


def main():
    validate_user_input()


main()
