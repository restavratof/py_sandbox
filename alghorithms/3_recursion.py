# Factorial

num = 5

# Recursion
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

# Loop
def fact_loop(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

print(f'Recursion: {fact(num)}')
print(f'Loop     : {fact_loop(num)}')

