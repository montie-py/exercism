vocals = ['a', 'e', 'i', 'o', 'u', 'y']
def translate(text):
    split_text = text.split(' ')
    if len(split_text) == 1:
        return logic(text)
    else:
        return ' '.join([logic(slice) for slice in split_text])
    

def logic(text):
    if any(text.find(entry) == 0 for entry in ['xr', 'yt']):
        return rule1(text)
    return rule2(text)
    
def rule1(text):
    return text + 'ay'

def rule2(text):
    vocals_loc = vocals[:]
    if text[0] == 'y':
        vocals_loc = vocals[:-1]
    list_text = list(text)
    list_text_after = list_text[:]
    index = 0
    pass_vocal = False
    for symbol in list_text:
        if symbol not in vocals_loc or pass_vocal:
            list_text_after = list_text_after[1:] + list_text_after[:1]
            if symbol == 'q' and list_text[index+1] == 'u':
                pass_vocal = True
            else:
                pass_vocal = False
            index += 1
        else:
            break
    text = ''.join(list_text_after)
    return rule1(text)
    