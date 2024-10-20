# Prompt the user to enter two or more numbers
def perform_calculation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
# Different conditionals/ calculation   
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
                return
        else:
            print("Invalid operation.")
            return

        equation = f"{num1} {operation} {num2} = {result}"
        print(equation)
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    except ValueError:
         print("Invalid input. Please enter a number.")

def print_previous_calculations():
    try:
        with open("equations.txt", "r") as file:
            equations = file.readlines()
            for equation in equations:
                print(equation.strip())
    except FileNotFoundError:
        print("No previous calculations found.")

# Main program loop
while True:
    choice = input("Choose an option:\n1. Perform a calculation\n2. Print previous calculations\n3. Exit\n> ")
     
    if choice == '1':
        perform_calculation()
    elif choice == '2':
        print_previous_calculations()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
