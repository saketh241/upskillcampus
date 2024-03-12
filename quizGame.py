questions = {"1. What is the maximum length of a Python identifier?":"A",
"2. How is a code block indicated in Python?":"D",
"3. Which of the following is the proper syntax to check if a particular element is present in a list?":"A",}

options = [["A. No fixed lenght","B. 32","C. 134","D. 60"],
        ["A. Semi colon","B. Key","C. Bracket","D. Indentation"],
        ["A. Both C and D","B. While loop","C. if ele in list","D. if not ele not in list"],

]
#print the questions with options
def print_qustions():
    question_number = 1
    check_guesses = []
    correct_ans = 0
    for key in questions.keys():
        print("------------------------------------------------------------------------------------------------------------")
        print(key)
        print("------------------------------------------------------------------------------------------------------------")
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter you choice: ").upper()
        check_guesses.append(guess)
        correct_ans += check_answer(questions.get(key),guess)
        question_number+=1
    print("----------------------------------")

    display_score(correct_ans,check_guesses)
    print()


def check_answer(answer,guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0 


def display_score(correct_ans,picked_guesses):
    print("Correct Answers: ",end="")
    for key in questions:
        print(questions.get(key),end=" ")
    print()
    print("Guessed answers: ",end="")
    for i in picked_guesses:
        print(i,end=" ")
    print()
    
    print(f"You scored: {correct_ans}/{len(questions)}")


print_qustions()
