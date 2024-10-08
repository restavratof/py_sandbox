var1 = 1
var2 = 'b'
var3 = 'c'
str1 = '|{:<5d} | {:^5s} | {:>5s}|'.format(var1, var2, var3)
print(str1)

str2 = '|{v1:<5d} | {v2:<5s} | {v3:<5s}|'.format(v1=var1, v2=var2, v3=var3)
print(str2)

str3 = f'|{var1:>5d} | {var2:>5s} | {var3:>5s}|'
print(str3)


print('|%-5s | %5s | %5s|' % (var1, var2, var3))





