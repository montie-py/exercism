def is_valid(isbn):
    if not isbn or any(char.isalpha() for char in isbn[:-1]):
        return False

    if not(isbn[-1] == "8" or isbn[-1] == 'X'):
        return False

    isbn_list = [int(char) for char in isbn[:-1] if char.isdigit()]
    if len(isbn_list) != 9:
        return False

    if isbn[-1] == 'X':
        isbn_list.append(10)
    else:
        isbn_list.append(int(isbn_list[-1]))

    countdown = 10
    result = 0
    for digit in isbn_list:
        result += digit * countdown
        countdown -= 1

    return (result % 11) == 0
        