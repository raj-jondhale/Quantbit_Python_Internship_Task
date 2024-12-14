# Task 5 Validate user input as an integer
def validate_integer_input():
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        print(f"You entered: {int(user_input)}")
    else:
        print("Invalid input. Please enter a number.")


validate_integer_input()
