#private variable

_private_number = 10
print(_private_number)

#Strong private
__private_no = 20
print(__private_no)

#keywords

import keyword
print(keyword.kwlist)

#address of element
print(id(__private_no))

#convert to binary
x = 10

print('-'*100)
print('convert to binary')
print(bin(x))
print('-'*100)

print('-'*100)
print('convert to octal')
print(oct(x))
print('-'*100)

print('-'*100)
print('convert to hexa')
print(hex(x))
print('-'*100)

print('-'*100)
print('Float')
print('These cannot be represented in bin,hex,or oct')
print(1.2e4)
print('-'*100)

print('-'*100)
print('complex')
y = (2+3j)
print(y)
print(y.real)
print(type(2+3j))
print('-'*100)

print('-'*100)
print('Strings')

name = 'Sachin'
print(name[1:2])
print(name[:])
print('-'*100)

print('-'*100)
print('Python cannot convert complex type to int')
try:
    print(int("10.2"))
except:
    print(r'ValueError: invalid literal for int() with base 10: "10.2"')
print('-'*100)

#If we want to convert str type to int type,
# compulsary str should contain only integral value and should be specified in base-10

"""
bool(0)==>False
 2) bool(1)==>True 
 3) bool(10)===>True 
 4) bool(10.5)===>True 
 5) bool(0.178)==>True 
 6) bool(0.0)==>False 
 7) bool(10-2j)==>True 
 8) bool(0+1.5j)==>True 
 9) bool(0+0j)==>False 
 10) bool("True")==>True 
 11) bool("False")==>True 
 12) bool("")==>False
"""

print('-'*100)
#for bytes only allowed numbers are 0 to 256
by_val = [10,20,30,40]
print(by_val)
by_val = bytes(by_val)
print(by_val)
for v in by_val:
    print(v)
# by_val[1] = 30
# TypeError: 'bytes' object does not support item assignment

print('-'*100)

# bytearray is exactly same as bytes data type except that its elements can be modified.
print('-'*100)
by_arr = [10,20,30,40]
by_arr = bytearray(by_arr)
print('Before changing')
print(by_arr)
print('After changing')
by_arr[0] = 11
print(by_arr)
for val in by_arr:
    print(val)
print('-'*100)

for i in range(10):
    print(i)
print('-'*100)

my_set = set(list(range(10)))
print(my_set)
# my_set[0] = 12
# print(my_set)
# TypeError: 'set' object does not support item assignment

print('-'*100)

my_fset = frozenset(set(list(range(20))))
print(my_fset)

# my_fset[0] = 11
# print(my_fset)
# TypeError: 'frozenset' object does not support item assignment
# my_fset.add(0)
# print(my_fset)
# It is exactly same as set except that it is immutable.
