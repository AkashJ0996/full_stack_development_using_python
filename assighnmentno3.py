#1. Write a python script to convert a number into str type.
x=15
y=30

print("Result in str format : ")
print(str(x))
print(str(y))
print("Result of addition of two converted int valuse in str format :")
print(str(x)+str(y))
print()

#2. Write a python script to print Unicode of the character ‘m’
x='m'

print("Result in Unicode format : ")
print(ord(x))
print()

#3. Write a python script to print character representation of a given unicode 100.
ab=100

print("Result in chr format : ")
print(chr(ab))
print()

#4. Write a python script to print any number and its binary equivalent
num=81
print(num)

print("Result in binary format : ")
print(bin(num))
print()

#5. Write a python script to print any number and its octal equivalent.
num_2=255
print(num_2)

print("Result in Octal format : ")
print(oct(num_2))
print()

#6. Write a python script to print any number and its hexadecimal equivalent.
num_3= 205
print(num_3)

print("Result in Hexadecimal format : ")
print(hex(num_3))
print()

"""7. Write a python script to store binary number 1100101 in a variable and print it in
decimal format."""

num_4=0b1100101

print("Result in decimal format : ")
print(num_4)
print()

"""8. Write a python script to store a hexadecimal number 2F in a variable and print it in
octal format."""
num_5=0x2F

print("Result in Octal format : ")
print(oct(num_5))
print()

"""9. Write a python script to store an octal number 125 in a variable and print it in binary
format."""
num_5=0o125

print("Result in binary format : ")
print(bin(num_5))
print()

"""10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format."""
num1=0o25
num2=0x39
result=num1+num2

print("Result in binary format : ")
print(bin(result))
print()
