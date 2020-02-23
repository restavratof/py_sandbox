

var1 = 1
var2 = 'b'
var3 = 'c'
str = '|{:<5d} | {:^5s} | {:>5s}|'.format(var1, var2, var3)
print(str)

str = '|{v1:<5d} | {v2:^5s} | {v3:>5s}|'.format(v1=var1, v2=var2, v3=var3)
print(str)