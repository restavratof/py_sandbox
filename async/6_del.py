
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


# @coroutine
def sub_gen():
    while True:
        try:
            msg = yield
        except StopIteration:
            # print('Bla Bla')
            break
        else:
            print('......', msg)
    return 'STR1'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
