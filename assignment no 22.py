#1. Write a recursive python function to calculate sum of first N natural numbers

def sum(n):
   if n==1:
     return 1
   return n+sum(n-1)
n=int(input("enter N no. : "))
result=sum(n)
print("sum of first %d no is %d "%(n,result))
print()

#2. Write a recursive python function to calculate sum of first N odd natural numbers

def sum_of_odd(n):
    if n==1:
       return 1
    return ((2*n)-1)+sum_of_odd(n-1)
n=int(input("enter the number : "))
result2=sum_of_odd(n)
print("sum of first %d odd natural no is %d "%(n,result2)) 
print()

#3. Write a recursive python function to calculate sum of first N even natural numbers

def sum_of_e1(n):
    if n==1:
       return 2
    return (2*n)+sum_of_e1(n-1)
n=int(input("enter the number "))
result3=sum_of_e1(n)
print("sum of first %d even natural no is %d "%(n,result3)) 
print()

"""4. Write a recursive python function to calculate sum of squares of first N natural
numbers"""

def sum_of_sq(n):
    if n==1:
       return 1
    return (n**2)+sum_of_sq(n-1)
n=int(input("enter the number "))
result4=sum_of_sq(n)
print("sum of first %d square natural no is %d "%(n,result4)) 
print()

#5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def sum_of_cube(n):
    if n==1:
       return 1
    return (n**3)+sum_of_cube(n-1)
n=int(input("enter the number "))
result5=sum_of_cube(n)
print("sum of first %d cubes natural no is %d "%(n,result5)) 
print()

#6. Write a recursive python function to calculate the factorial of a number.

def fct(n):
   if n==0:
      return 1
   return n*fct(n-1)
n=int(input("enter the number "))
result6=fct(n)
print("Factorial of %d no is %d "%(n,result6)) 
print()

#7. Write a recursive python function to calculate sum of the digits of a given number

def sum_of_digit(n):
   if n!=0:
     return n%10 + sum_of_digit(n//10)
   else:
     return n

n=int(input("enter the number :"))
result7=sum_of_digit(n)
print("Sum of Digit is : ",result7) 
print()

#8. Write a recursive python function to print binary of a given decimal number.

def dec_to_bin(n):
    if n==0:
       return 0
    return ((n%2)+10*dec_to_bin(n//2))

n=int(input("enter the number :"))
result8=dec_to_bin(n)
print("decimal of %d is binary %d "%(n,result8))
print()

#9. Write a recursive python function to print octal of a given decimal number

def dec_to_oct(n):
    if n==0:
       return 0
    return ((n%8)+10*dec_to_oct(n//8))

n=int(input("enter the number :"))
result9=dec_to_oct(n)
print("decimal of %d is octal %d"%(n,result9)) 
print()

#10. Write a recursive python function to find the Nth term of the Fibonacci series.

def fb_series(n):

    if n==1:
       return 0
    elif n==2:
       return 1
    else:
       while n>0:
          return fb_series(n-1)+fb_series(n-2)
n=int(input("enter the number : "))
fib=fb_series(n)
print("at %d th place %d element is present in fibonacci series "%(n,fib))
print()
