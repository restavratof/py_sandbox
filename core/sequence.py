# Lists
print('-'*79)
print('Lists:')

print('\nCopy:')
list_a = ['a1', 'a2', 'a3']
list_c = list_a
print(f'list_a: {list_a}')
print(f'list_c: {list_c}')
list_c[1] = "a21"
print('After:')
print(f'list_a: {list_a}')
print(f'list_c: {list_c}')

print('\nReversed:')
print(list(reversed(list_a)))




