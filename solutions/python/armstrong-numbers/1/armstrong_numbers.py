def is_armstrong_number(number):
    if number < 10:
        return True
    str_number = str(number)
    power = len(str_number)
    total_sum = 0

    for digit in str_number:
        total_sum += int(digit) ** power

    if number == total_sum:
        return True

    return False
