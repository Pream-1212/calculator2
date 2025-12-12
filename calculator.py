"""
A simple command line calculator that performs addition and substraction
"""


def get_numbers():
  # get number from user input
  numbers = []
  print("Enter numbers (type 'done') when finished): ")
  while True:
    user_input = input("Enter a number: ").strip()
    if user_input.lower() == 'done':
      break
    try: 
      number = float(user_input)
      numbers.append(number)
    except ValueError:
      print("Invalid input please enter a number")
  return numbers    


def main():
  # function to run the calculator
  print("=" * 50)
  print("Welcome to the collaborative")
  print("a" * 50)
  numbers = get_numbers()
  if len(numbers) == 0:
    print("No numbers entered exiting")
    return
  print(f"\n You entered: {numbers}")
  print("\n what operation would you like to perform?")
  print("1. Add")
  print("2. Multiply")
  Choice = input("Enter your choice (1 or 2): ")
  # There are other implementation needed here


if __name__ == "__main__":
  main()


