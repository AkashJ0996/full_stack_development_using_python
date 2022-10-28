#1. Write a python script to reverse a number.
num = int(input("Enter a num : "))
R_num = 0

while num != 0:
    d=num % 10
    R_num = R_num * 10 + d
    num //= 10
print("Reversed Number: ",R_num )
print()

num = str(input("Enter a num : "))
print (num[::-1])
print()

#2. Write a python script to check whether a given number is Prime or not

num = int(input("Enter any number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("%d is not a prime number"%num)
            break
    else:
        print("%d is a prime number"%num)
else :
    print("%d is not a prime number"%num)
print()

#3. Write a python script to print all Prime numbers under 100

for n in range (1, 101):
    count = 0
    for i in range(2, n):
        if(n % i == 0):
            count = count + 1
            break

    if (count == 0 and n != 1):
        print(n, end=' ')
print()

"""4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""

n=int(input("Enter the first no : "))
m=int(input("Enter the second no : "))
for n in range (n, m):
    count = 0
    for i in range(2, n):
        if(n % i == 0):
            count = count + 1
            break

    if (count == 0 and n != 1):
        print(" %d" %n)
print()

#5. Write a python script to find next prime number of a given number

n=int(input("Enter the n no : "))
if n > 0 :
    while True:
        n += 1
        for i in range(2,n,1):
            if n % i == 0 :
                break
        else:
            print(n)
            break
print()

#6. Write a python script to print first N prime numbers

n=int(input("Enter the n no : "))
for n in range (1, n+1):
    
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        print(n, end=' ')
print()

"""7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not."""

n=int(input("Enter the first no : "))
m=int(input("Enter the second no : "))

mn = min(n,m) 
for i in range(1, mn+1): 
    if n%i==0 and m%i==0: 
       gcd = i 

#no is said to be co-prime if greatest common divisor is equal to 1 
if gcd == 1: 
    print("Yes! No entered are Co-Prime.") 
else: 
     print("No entered are not Co-Prime.")
print()

#8. Write a python script to print first N terms of a Fibonacci series
n = int(input ("How many terms the user wants to print : "))  
  
n1 = 0  # First two default terms  0 , 1
n2 = 1  
count = 1
sum = 0
print("fibonacci series : ",sep=",")
while(count<=n):
    print (sum,end=" ")
    count += 1
    n1 = n2
    n2 = sum 
    sum = n1 +n2
print()

#9. Write a python script to calculate LCM of two numbers

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if(x>y):
    min_no=x
else:
    min_no=y
while(1):
    if(min_no%x==0 and min_no%y==0):
        print("LCM is:",min_no)
        break
    min_no=min_no+1
print()

#10. Write a python script to calculate HCF of two numbers

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if(x>y):
    min_no=x
else:
    min_no=y
for i in range(1,min_no+1):
    if(x%i==0 and y%i==0):
        hcf=i
print("HCF is:",hcf)

print()