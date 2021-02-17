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