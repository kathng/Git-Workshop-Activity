first = int(input("Enter your first operand: "))
second = int(input("Enter your second operand: "))

def add(operand_1, operand_2):
    # TODO: Calculate the sum of the 2 operands and return it
    result = first + second
    print("The result is", result)
    return result

add(first, second)
