def rotate(text, key):
    text_list = []
    upper_start = 65
    upper_end = 91
    lower_start = 97
    lower_end = 123
    for char in text:
        element = ''
        if char.isalpha():
            if char.isupper():
                start = upper_start
                end = upper_end
            else:
                start = lower_start
                end = lower_end
                
            mainsum = ord(char) + key
            
            if mainsum >= end:
                mainsum += start
            element = chr(mainsum % end)
        else:
            element = char
        text_list.append(element)
    return ''.join(text_list)
