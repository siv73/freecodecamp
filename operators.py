a = 10
b = 2
print(a/b)
#a/b gives float
print(a//b)
#above gives int
print(a%b) #0
print(a**b) #100

x = 10.5
y = 2.5

print(x/y)
print(x//y) #4.0 not 4! remeber!

print(4==4.0) #true so both are same.

print(bool(10)==True)

print("siva" and "Sivasai") #sivasai

print("" and "siva") #"" 

#bitwise operators
#only applicable for int and boolean types
print(4 & 5) #4 is the answer!

# print(10.2 & 4.6) TypeError: unsupported operand type(s) for &: 'float' and 'float'

print(4^4) #0
print(4^5) #1 basically this means that both should be different

print(bool(4^5)) #true!

print(~20) #-21 is the answer

print(~-20) #19 is the answer!

print(~True) #-2 is the answer
print(~False) #-1 is the answer

print(bin(10))  #00001010 is binary notatio

print(10<<2) # here, leading 00 is removed then 00101000 is the resultant

x = bin(10)
print(x.isdigit()) #false

print(bin(1))
print(bin(True))
print(1 << 4)

print(5 << 2)
print(7<<2)

print(10&5)
print(5&10)
print(4 & 5)
print(9&10)
print(10&8)

# x = int(input("Please enter input"))
# y = int(input("Please enter input"))

# min = x if x < y else y
# print(min , 'is the minimum of both')

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:")) 
# c=int(input("Enter Third Number:")) 
# min=a if a<b and a<c else b if b<c else c 
# print("Minimum Value:",min)

#We can use is operator for address comparison where as == operator for content comparison.

import math
print(math.ceil(4.2)) #5
print(math.floor(4.9)) #4
print(math.pow(4,100))
print(math.trunc(math.pow(4,10))) #removes float point?
print(math.trunc(4.5)) #4 yes!
print(math.pow(4,10))
print(math.gcd(20,25))
# print(math.lcm(20,25))not present!

def area_circle(radius):
    return math.pi * math.pow(radius,2)

print(area_circle(7))