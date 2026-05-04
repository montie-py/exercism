def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    factors = [factor for factor in range(1, number) if number % factor == 0]

    total = sum(n for n in factors)
    
    if total == number:
        return "perfect"
    elif total < number:
        return "deficient"
    
    return "abundant"