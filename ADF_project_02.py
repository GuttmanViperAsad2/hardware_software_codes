def main():
    print("Hello and welcome to Project02.")
    print("My name Alpha1 and I will be asking you a 4 riddles.")
    print("Fail to get the right answers and the question repeat itself until you get it right.")
    print("If you don't want to answer anymore then type Exit.")
    count = 0
    run_loop = question()

    while run_loop !='Exit':
        run_loop = question()
def guess():

def question():
    print("Riddle 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind, what am I?")
    riddle_answer = "An Echo"
    guess = ""
    guess_count = 0

while guess != riddle_answer:
    guess = input("Enter guess: ")
    guess_count += 1

    print("Riddle 2: I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?")
    riddle_answer = "Your Breath"
    guess = ""
    guess_count = 0

while guess != riddle_answer:
    guess = input("Enter guess: ")
    guess_count += 1


    print("Riddle 3: I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?")
    riddle_answer = "A Keyboard"
    guess = ""
    guess_count = 0

while guess != riddle_answer:
    guess = input("enter guess: ")
    guess_count += 1


    print("Riddle 4: The more of this there is, the less you see. What is it?")
    riddle_answer = "Darkness"
    guess = ""
    guess_count = 0

while guess != riddle_answer:
    guess = input("enter guess: ")
    guess_count += 1


def conversation():
    print("Congrats, You answered all of my riddles correctly!!")
    conversation()
def exit():
    quit()

if __main__ == "__main__":
    main()
