mylist = [10, 20, 30]
new_items = [40, 50, 60]
mylist += new_items
print(mylist)

print('1','-'*50)
mylist = [10, 20, 30]
print(mylist + new_items)

print('2','-'*50)
mylist = [10, 20, 30]
t = (40, 50, 60)
mylist += t
print(mylist)

print('3','-'*50)
mylist = [10, 20, 30]
t += mylist
print(t)
print('1','-'*50)

print('1','-'*50)

#------------------------------------------
#  +
#   calls __add__ method of object.
#   Where it add object from right side to object on left side.
#   !!! Allows only for objects the same type.
#
#------------------------------------------
# +=
#   calls __iadd__ method of object.
#   Where it iterates over object on right side and add every item to object on left side.
#   !!! If object on left side has the method implemented,
#       then it allowed to use on right side any ITERATABLE object
#