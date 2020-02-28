
def subgen():
    x = 'Ready'
    msg = yield x
    print('Subgen received:', msg)