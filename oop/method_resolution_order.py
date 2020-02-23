
class A(object): pass

class B(A): pass

class C(A): pass

class BC(B, C): pass

print(BC.__mro__)
# (__main__.BC, __main__.B, __main__.C, __main__.A, object)


print(list.__mro__)
# (list, object)

help(BC)