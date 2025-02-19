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
    print("Hello user, today we will be doing convertion.")
    print("We will be converting binary to decimal and vice versa")
    choice()
def choice():
     print("Choose to convert binary to decimal or vice versa")
     print("Type (a) to convert decimalto binary or (b) to convert binary to decimal")
     option = input()
     if option == "a":
         binary_to_decimal()
     elif option == "b":
         decimal_to_binary()
     elif option == "exit":
         exit()
def binary_to_decimal(binary_str):
  decimal_value = 0
  power = 0
  for digit in reversed(binary_str):
      if digit == '1':
          decimal_value += 2 ** power
      elif digit != '0':
          raise ValueError("Invalid binary string: contains non-binary characters")
      power += 1
      return decimal_value
binary_input = int(input("Enter a binary number: "))
decimal_output = binary_to_decimal(binary_input)
print("The decimal representation of {binary_input} is {decimal_output}")
choice()
decimal_to_binary()

def decimal_to_binary(decimal_num):
  if decimal_num == 0:
        return "0"
  binary_string = ""
  while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string
        decimal_num //= 2
  return binary_string
decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print("The binary representation of {decimal_input} is {binary_output}")
choice()


def exit():
    print("Calculation Stopped!")
    quit()
if __name__ == "__main__":
    main()
