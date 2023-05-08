from Arithmetic import Arithmetic

class user():
    print("Welcome to the Arithmetic Class calculator!\n"
          "Please choose the operation you want to perform:\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", Arithmetic.addition(a, b))

    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", Arithmetic.subtraction(a, b))

    elif choice == 3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", Arithmetic.multiplication(a, b))

    elif choice == 4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", Arithmetic.division(a, b))

    else:
        print("Invalid choice. Please try again.")