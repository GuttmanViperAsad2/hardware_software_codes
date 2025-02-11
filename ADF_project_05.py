def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            exit()
        if is_valid_integer(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")
def is_valid_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
def main():
  print("We are adding and subtracting Two whole numbers")
  print("type 'exit' to stop")
  choice()
def choice():
     print("Choose whether you will be adding or subtracting")
     print("Type (a) for adding or (b) for subtracting")
     option = input()
     if option == "a":
         calc1()
     elif option == "b":
         calc2()
     elif option == "exit":
         exit()
def calc1():
  x = get_valid_input("Enter first whole number: ")
  y = get_valid_input("Enter second whole number: ")
  sum = int(x) + int(y)
  print("{} + {} = {}". format(x, y, sum))
  choice()
  calc2()
def calc2():
  x = get_valid_input("Enter first whole number: ")
  y = get_valid_input("Enter second whole number: ")
  sum = int(x) - int(y)
  print("{} - {} = {}". format(x, y, sum))
  choice()

def exit():
    print("Calculation Stopped!")
    quit()
if __name__ == "__main__":
    main()
