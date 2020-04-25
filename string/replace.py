# str.replace(old, new[, max])
# Parameters
#     old − This is old substring to be replaced.
#     new − This is new substring, which would replace old substring.
#     max − If this optional argument max is given, number of replacements. By default will replace all.

str1 = 'This is a very long string for testing replace() function with Python!'

print(f'ORIG: {str1}')
print(f' 1  : {str1.replace("i","A", 2)}')
