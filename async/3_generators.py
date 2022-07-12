from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)  # milliseconds
        yield pattern.format(str(t))


def gen1(s):
    for gi in s:
        yield gi


def gen2(n):
    for gi in range(n):
        yield gi


g1 = gen1('oleg')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
