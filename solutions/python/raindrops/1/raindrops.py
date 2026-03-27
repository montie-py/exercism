import operator

def convert(number):
    result = ""

    if not operator.mod(number, 3):
        result += "Pling"

    if not operator.mod(number, 5):
        result += "Plang"

    if not operator.mod(number, 7):
        result += "Plong"

    if not result:
        result = str(number)

    return result