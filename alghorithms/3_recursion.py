"""Factorial"""
num = 5


def fact(x):
    """Recursion way"""
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


def fact_loop(x):
    """Loop way"""
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


print(f'Recursion: {fact(num)}')
print(f'Loop     : {fact_loop(num)}')
