def main():
    print("Hello and welcome to Project02.")
    print("My name Alpha1 and I will be asking you a 4 riddles.")
    print("Fail to get the right answers and the question repeat itself until you get it right.")
    print("If you don't want to answer anymore then type Exit.")

def answer_traker():
    question_count = 0
def increment_and_get_count():
        nonlocal question_count
        question_count += 1
        return question_count

    return increment_and_get_count()

track_questions = answer_tracker()

print("Question", track_questions())
print("Question", track_questions())
print("Question", track_questions())
print("Question", track_questions())

def question1():
    print("Riddle 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind, what am I?")
    answer = input().lower().strip()
    if answer == "An Echo":
        print("CORRECT")
    elif answer == "exit":
        exit()
    else:
        print("Wrong Answer, Try Again!")
        question1()

def question2():
    print("Riddle 2: I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?")
    answer = input().lower().strip()
    if answer =="Your Breath":
        print("CORRECT")
    elif answer == "exit":
        exit()
    else:
        print("Wrong Answer, Try Again!")
        question2()

def question3():
    print("Riddle 3: I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?")
    answer = input().lower().strip()
    if answer =="A Keyboard":
        print("CORRECT")
    elif answer == "exit":
        exit()
    else:
        print("Wrong Answer, Try Again!")
        question3()

def question4():
    print("Riddle 4: The more of this there is, the less you see. What is it?")
    answer = input().lower().strip()
    if answer =="Darkness":
        print("CORRECT")
    elif answer == "exit":
        exit()
    else:
        print("Wrong Answer, Try Again!")
        question4()

def conversation():
    print("Congrats, You answered all of my riddles correctly!!")
    conversation()
def exit():
    quit()

if __main__ == "__main__":
    main()
