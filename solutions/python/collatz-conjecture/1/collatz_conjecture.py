def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_result = 0;
    if number != 1:
        while (True):
            if int(number) == 1:
                return steps_result
            steps_result +=1 
            if number % 2 == 0:
                number /= 2
            else:
                number = number * 3 + 1
    return steps_result