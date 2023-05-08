class Arithmetic():
    result = 0

    def addition(firstnumber, *numbers):

        for index, number in enumerate(numbers):
            if index == 0:
                result = firstnumber + number
            else:
                result += number
        return result
    
    def subtraction(firstnumber, *numbers):

        for index, number in enumerate(numbers):
            if index == 0:
                result = firstnumber - number
            else:
                result -= number
        return result

    def multiplication(firstnumber, *numbers):

        for index, number in enumerate(numbers):
            if index == 0:
                result = firstnumber * number
            else:
                result *= number
        return result
    
    def division(firstnumber, *numbers):

        for index, number in enumerate(numbers):
            if index == 0:
                result = firstnumber / number
            else:
                result /= number
        return result