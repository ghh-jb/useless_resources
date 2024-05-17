def get_dividers(num:int) -> list:
    # num = abs(num)
    dividers = [num]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dividers.append(i)
            dividers.append(num // i)
    return dividers
