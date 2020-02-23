
print('---------------------------------------------------')
# STANDARD
res1 = []
for x in range(1, 25, 2):
    res1.append(x)

print("RESULT 1:{}".format(res1))


print('---------------------------------------------------')
# LIST COMPREHENSIONS
res2 = [x for x in range(1, 25, 2)]

print("RESULT 2:{}".format(res2))

print('---------------------------------------------------')
# LIST COMPREHENSIONS 2
res3 = list(map(lambda  x: x, range(1, 25, 2)))

print("RESULT 3:{}".format(res3))
