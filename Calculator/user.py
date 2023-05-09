from Arithmetic import Arithmetic


class User():
    def run_user(self):
        print("Welcome to the Arithmetic Class calculator!\n"
              "Please choose the operation you want to perform:\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide")

        choice = int(input("Enter your choice (1/2/3/4): "))
        value_input = input(
            'Enter operation values separated by spaces: ').split(' ')

        # converte valores para int
        value_input = [int(x) for x in value_input]

        if choice == 1:
            result = Arithmetic.addition(*value_input)
            print("Result:", result)

        elif choice == 2:
            result = Arithmetic.subtraction(*value_input)
            print("Result:", result)

        elif choice == 3:
            result = Arithmetic.multiplication(*value_input)
            print("Result:", result)

        elif choice == 4:
            result = Arithmetic.division(*value_input)
            print("Result:", result)

        else:
            print("Invalid choice. Please try again.")
