#1. Write a python script to check whether a given number is positive or non-positive
x=int(input("Enter the number : "))
if x>0 :
    print("Entered Number %d is positive "%x)
else:
    print("Entered Number %d is negative "%x)
print()    

#2. Write a python script to check whether a given number is divisible by 5 or not
y=int(input("Enter the number : "))
if y%5==0 :
    print("Entered Number %d is divisible by 5 "%y)
else:
    print("Entered Number %d is not divisible by 5 "%y)
print()  

#3. Write a python script to check whether a given number is even or odd
z=int(input("Enter the number : "))
if z%2==0 :
    print("Entered Number %d is Even"%z)
else:
    print("Entered Number %d is Odd "%z)
print()

"""4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b: 
     print("Fisrt number %d is greater than the second number."%a)  
elif a == b :    
     print("numbers are equal.")       
else:   
     print("Second number %d is greater than the First number."%b)
print()

#5. Write a python script to print two given words in dictionary order
a=((input("enter two names :")))
b=((input("enter two names :")))

if a<b:
    print(a,b)
else :
    print(b,a)
print()

#6. Write a python script to check whether a given number is a three digit number or not.
n=int(input("Enter a number:"))
if(n < 1000 and n > 99):
    print("%d is a 3 digit number "%n)
else:
    print("%d is not a 3 digit number"%n)
print()

#7. Write a python script to check whether a given number is positive, negative or zero.
n1 = int(input("Enter a number: "))
if n1> 0:
   print(" You entered %d which is Positive number"%n1)
elif n1 == 0:
   print(" You entered (%d) Zero"%n1)
else:
   print("You entered %d which is Negative number"%n1)
print()

"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
import math
a = int(input('Enter values of a: '))
b = int(input('Enter values of b: '))
c = int(input('Enter values of c: '))

d = b*b - 4*a*c

if d > 0:
    r1 =  - (b + math.sqrt(d)) / (2 * a)
    r2 =  - (b - math.sqrt(d)) / (2 * a)
    print('Roots are real & distinct, Root1 =',r1,' Root2 = ',r2)
elif d == 0:
    r1 = ( - b) / (2 * a)
    r2 = r1
    print('Roots are real & equal, Root1 =',r1,' Root2 = ',r2)
else:
    print('Roots are imaginary')
print()

#9. Write a python script to check whether a given year is a leap year or not.
y=int(input("enter the year: "))

if y%4==0:
    print("Your entered year %d is a Leap year "%y)
else:
    print("Your entered year %d is not a Leap year "%y)
print()

"""10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
 
if (n1 > n2) and (n1 > n3):
   greatest = n1
elif (n2 > n1) and (n2 > n3):
   greatest = n2
else:
   greatest = n3
 
print("The largest number is",greatest)
print()

"""11. Write a python script to take the month value in numeric format and display the
number of days in it."""
month_no=int(input("the no. of Month: "))

if month_no == 2 :
	print("No. of days: 28/29 days ")
elif month_no in ( 4 , 6 , 9 , 11 ):
	print("No. of days: 30 days")
elif month_no in ( 1 , 3 , 5 , 7 , 8 , 10 , 12):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 
print()

"""12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

x=complex(input("Enter a number : "))
if x.real > x.imag:
    print("greatest number in given complex no is real part no which is : ",x.real)
else:
    print("greatest number in given complex no is imaginary part no which is : ", x.imag)
print()
