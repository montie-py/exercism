def is_pangram(sentence):
    sentence_set = {character for character in sentence.lower() if character.isalpha()}
    return len(sentence_set) == 26