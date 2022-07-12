

def add(a, b):
    """This function adds two numbers"""
    return a+b


sum1 = add(1, 3)
print("Access docstring method 1:", add.__doc__)
print("Access docstring method 2:", end="")
help(add)
