
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def sub_gen():
    x = 'Ready'
    msg = yield x
    print('SubGen received:', msg)


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    summa = 0
    result = None

    while True:
        try:
            x = yield result
        except StopIteration:
            print('End')
        except BlaBlaException:
            print('--------------------')
        else:
            count += 1
            summa += x
            result = round(summa/count, 2)
