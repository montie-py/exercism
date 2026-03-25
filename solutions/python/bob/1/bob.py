def response(hey_bob):
    is_question = False
    if hey_bob and hey_bob.strip():
        is_question = '?' == hey_bob.strip()[-1]
        
    has_whitespace = any(char.isspace() for char in hey_bob)
    #is_question = hey_bob and ('?' == hey_bob[-1])
    is_upper = (hey_bob.upper() == hey_bob) and any(char.isalpha() for char in hey_bob)
    is_empty = not hey_bob
    has_unusual_space = any(char.isspace() for char in hey_bob if char != " ") or not hey_bob.strip()
    
    if is_question and not is_upper:
        response = "Sure."
    elif is_upper and not is_question:
        response = "Whoa, chill out!"
    elif is_upper and is_question:
        response = "Calm down, I know what I'm doing!"
    elif is_empty or has_unusual_space:
        response = "Fine. Be that way!"
    else:
        response = "Whatever."

    return response
    
