# https://forum.dabeaz.com/t/lambda-calculus-pycon-2019/408

# --------------------------------------------------------------------------
print('-'*100)
print('-', 'MAP()')

nums = (1,2,3,4)


def multiply(n):
    return n * n


result = map(multiply, nums)
print(f'1   : {list(result)}')

result = map(lambda x: x*x, nums)
print(f'2   : {list(result)}')


# --------------------------------------------------------------------------
print('-'*100)
print('-', 'FILTER()')


def my_filter(n):
    if n > 2:
        return 1
    else:
        return 0


result = filter(my_filter, nums)
print(f'3   : {list(result)}')

test1 = [1, 'a', 0, False, True, '0']
result = filter(None, test1)
print(f'4   : {list(result)}  from  {test1}')

# --------------------------------------------------------------------------
print('-'*100)
print('-', 'REDUCE()')
import functools as ft
result = ft.reduce(lambda x,y: x if x>y else y, nums)
print(f'MAX : {result}')

result = ft.reduce(lambda x,y: x+y, nums)
print(f'SUM : {result}')