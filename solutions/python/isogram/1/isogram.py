def is_isogram(string):
    string_l = [character for character in string.lower() if character.isalnum()]
    string_s = set(string_l)

    return len(string_l) == len(string_s)
