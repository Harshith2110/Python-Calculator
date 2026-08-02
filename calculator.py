# Python Calculator

while True:
    print("\n===== CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, //, %, **): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "//":
        if num2 != 0:
            print("Result =", num1 // num2)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "%":
        if num2 != 0:
            print("Result =", num1 % num2)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "**":
        print("Result =", num1 ** num2)

    else:
        print("Invalid operator!")

    choice = input("\nDo another calculation? (y/n): ")

    if choice.lower() != "y":
        print("Thank you for using Calculator!")
        break
