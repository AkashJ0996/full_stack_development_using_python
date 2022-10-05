#1.Write a python script to calculate sum of first N natural numbers

num = int(input("Enter the num : "))
sum = 0
while (num > 0) :
    sum = sum + num
    num = num-1
print("Sum of natural  numbers is :", sum)
print()

#2. Write a python script to calculate sum of squares of first N natural numbers
num = int(input("Enter the num : "))
sum = 0
while (num > 0) :
    sum = sum + num**2
    num = num-1
print("Sum of square numbers is :", sum)
print()

#3. Write a python script to calculate sum of cubes of first N natural numbers

num = int(input("Enter the num : "))
sum = 0
while (num > 0) :
    sum = sum + num**3
    num = num-1
print("Sum of cube numbers is :", sum)
print()

#4. Write a python script to calculate sum of first N odd natural numbers

n=int(input("enter a num : "))
sum = 0
for i in range(1,n+1) :
    if i%2 != 0:
      sum=sum+i
print("Sum of odd numbers from 1 to", n, "is :", sum)
print()

#5. Write a python script to calculate sum of first N even natural numbers

n=int(input("enter a num : "))
sum = 0
for i in range(1,n+1) :
    if i%2 == 0:
      sum=sum+i
print("Sum of even numbers from 1 to", n, "is :", sum)
print()

#6. Write a python script to calculate factorial of a given number

num=int(input("Enter a num : "))
factorial=1 
if num < 0:
   print("Enter positive num. there is no factorial of negative num")
elif num == 0:
   print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
       factorial = factorial*i
    print("The factorial of",num,"is",factorial)
print()

#7. Write a python script to count digits in a given number

num = int(input("Enter a num : "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: ",count)
print()

#8. Write a python script to calculate sum of digits of a given number

num=int(input("Enter a num : "))
sum = 0
for digit in str(num): 
    sum += int(digit)  
print("sum of digits: ",sum)
print()

"""9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""

print("Enter Decimal Number: ", end="")
dnum = int(input())
bnum = 0
mul = 1
while dnum>0:
    rem = dnum%2
    bnum = bnum+(rem*mul)
    mul = mul*10
    dnum = int(dnum/2)

print("\nEquivalent Binary Value =", bnum)
print()

"""10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""


print("Enter Octal Number: ", end="")
dnum = int(input())
onum = 0
mul = 1
while dnum>0:
    rem = dnum%8
    onum = onum+(rem*mul)
    mul = mul*10
    dnum = int(dnum/8)

print("\nEquivalent Octal Value =", onum)
print()

