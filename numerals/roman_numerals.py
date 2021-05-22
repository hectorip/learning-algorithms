def transform(roman):
    """Transforms a roman numeral into a decimal integer

    Rules:

    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D =  500
    M = 1000

    """
    values = {
        "": 0,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    prev = ""
    for curr in roman:
        curr_val = values[curr]
        prev_val = values[prev]
        if curr_val > prev_val:
            total += curr_val - (2 * prev_val)
        else:
            total += curr_val

        prev = curr

    return total