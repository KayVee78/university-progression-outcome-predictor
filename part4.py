# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1998488

# Date: 2023-04-21


# variable declaration
pass_credits = 0
pass_data = 0
defer_credits = 0
defer_data = 0
fail_credits = 0
fail_data = 0
total_credits = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
total_std = 0
data_dict = {}  # {{w1234567:{"pass": 120, "defer": 0, "fail": 0}}, {w1234567:{"pass": 120, "defer": 0, "fail": 0}}}
outcome = {}
student_id = ""
dict_key = ""


def progression_outcome(passs, defer, fail):  # function which determines progression
    # making the declared variables global, to use them throughout the program
    global pass_credits, defer_credits, fail_credits, total_credits, progress_count, trailer_count, retriever_count, \
        exclude_count, total_std, pass_data, defer_data, fail_data, data_dict, dict_key

    # implementing a while loop to break soon after the progression outcome is printed &
    # this also increments the specific counter
    while True:
        # searched about creating and reading values from a dictionary which is dynamically updated by user inputs from the internet (via w3schools, tutorialspoint & stackoverflow)
        # getting values relevant to the key from the dictionary 'data_dict'
        for dict_key in data_dict:
            get_values = data_dict.get(dict_key)
            pass_credits = get_values["pass"]
            defer_credits = get_values["defer"]
            fail_credits = get_values["fail"]

        # checking whether total is equal to 120
        if (passs+defer+fail) != 120:
            print('Total incorrect')
            break  # break loop -> if total is incorrect

        elif passs == 120:
            print('Progress')
            pass_data = f"{pass_credits}, {defer_credits}, {fail_credits}"
            outcome.update({dict_key: {"outcome": "Progress", "pass": pass_credits, "defer": defer_credits, "fail": fail_credits}})
            progress_count += 1
        elif passs == 100 and (defer == 0 or fail == 0):
            print('Progress(module trailer)')
            trailer_data = f"{pass_credits}, {defer_credits}, {fail_credits}"
            outcome.update({dict_key: {"outcome": "Progress(module trailer)", "pass": pass_credits, "defer": defer_credits, "fail": fail_credits}})
            trailer_count += 1
        elif passs <= 80 and (defer >= 40 or fail <= 60):
            print('Module retriever')
            retriever_data = f"{pass_credits}, {defer_credits}, {fail_credits}"
            outcome.update({dict_key: {"outcome": "Module retriever", "pass": pass_credits, "defer": defer_credits, "fail": fail_credits}})
            retriever_count += 1
        elif fail >= 80:
            print('Exclude')
            exclude_data = f"{pass_credits}, {defer_credits}, {fail_credits}"
            outcome.update({dict_key: {"outcome": "Exclude", "pass": pass_credits, "defer": defer_credits, "fail": fail_credits}})
            exclude_count += 1

        total_std += 1
        break


def validate_user_input():
    global pass_credits, defer_credits, fail_credits, student_id, data_dict, outcome

    while True:
        try:
            student_id = input('Please enter your student id\t: ')
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

        # updating 'data_dict' dictionary with user inserted values
        data_dict.update({student_id: {"pass": pass_credits, "defer": defer_credits, "fail": fail_credits}})

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

        # if proceeding_char is 'q' display dictionary 'outcome'
        if proceeding_char == 'q':
            print("Part 4: ")
            for outcome_key in outcome:
                get_outcome_values = outcome.get(outcome_key)  # getting values relevant to the key from the dictionary 'outcome_key'
                print(outcome_key, ":", get_outcome_values["outcome"], "-", get_outcome_values["pass"], "\b,", get_outcome_values["defer"], "\b,", get_outcome_values["fail"])
            break

        if proceeding_char == 'y':
            continue


def main():
    validate_user_input()


main()
