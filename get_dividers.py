# def get_dividers(num:int) -> list:
#     # num = abs(num)
#     dividers = [num]
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             dividers.append(i)
#             dividers.append(num // i)
#     return dividers
# ^^^ V1.0

def get_dividers(num:int) -> list:
    # num = abs(num)
    if num == 1:
        return [1]
    dividers = [1, num]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dividers.append(i)
            dividers.append(num // i)
    return list(set(dividers))
# ^^^ V1.1
