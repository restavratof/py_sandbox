
print('-'*50)
# STANDARD
res1 = []
for x in range(1, 25, 2):
    res1.append(x)

print("RESULT 1:{}".format(res1))


print('-'*50)
# LIST COMPREHENSIONS
res2 = [x for x in range(1, 25, 2)]

print("RESULT 2:{}".format(res2))

print('-'*50)
# LIST COMPREHENSIONS 2
res3 = list(map(lambda x1: x1, range(1, 25, 2)))

print("RESULT 3:{}".format(res3))

# -------------------------------------------------------------------------
print('-'*50)
print('-'*3, 'list  comprehension')
#   [ expression for x in iterable if condition ]
nums = [1, 2, 3, 4, 5, 6]
squares = [x*x for x in nums]
print(squares)

# Set comprehension:
#   { expression for x in iterable if condition }
# Dict comprehension:
#   { key:val for key, val in iterable if condition }

# -------------------------------------------------------------------------
print('-'*50)
print('-'*3, 'Iter powers')
# Generator expressions allow you to proceed a huge amount of data incrementally
#   saving a lot of memory.
squares = (x*x for x in nums)
print(squares)
