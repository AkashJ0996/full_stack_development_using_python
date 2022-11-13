#1. Write a recursive python function to print first N natural numbers.

def N_num(n):
   if n > 0:
     N_num(n - 1)
     print(n)
num = int(input("Enter N no. to print Natural no. :"))
N_num(num)
print()

#2. Write a recursive python function to print first N natural numbers in reverse order

def rev_N_num(n):
   if n > 0:
     print(n)
     rev_N_num(n - 1)
num2 = int(input("Enter N no. to print Natural no. in reverse order :"))
rev_N_num(num2)
print()

#3. Write a recursive python function to print first N odd natural numbers

def Odd_N_num(n):
   if n > 0:
     Odd_N_num(n - 1)
     print((2*n)-1)
num3 = int(input("Enter N no. to print Odd Natural no. :"))
Odd_N_num(num3)
print()

#4. Write a recursive python function to print first N odd natural numbers in reverse order

def RO_N_num(n):
   if n > 0:
     print((2*n)-1)
     RO_N_num(n - 1)
     
num4 = int(input("Enter N no. to print Odd Natural no. in reverse order :"))
RO_N_num(num4)
print()

#5. Write a recursive python function to print first N even natural numbers.

def e1_N_num(n):
   if n > 0:
     e1_N_num(n - 1)
     print(2*n)
num5 = int(input("Enter N no. to print Even Natural no. :"))
e1_N_num(num5)
print()

"""6. Write a recursive python function to print first N even natural numbers in reverse
order."""

def Re1_N_num(n):
   if n > 0:
     print(2*n)
     Re1_N_num(n - 1)
num6 = int(input("Enter N no. to print Even Natural no. in reverse order :"))
Re1_N_num(num6)
print()

#7. Write a recursive python function to print squares of first N natural numbers

def sq_N_num(n):
   if n > 0:
     sq_N_num(n - 1)
     print(n**2)
num7 = int(input("Enter N no. to print squares of first N Natural no. :"))
sq_N_num(num7)
print()

#8. Write a recursive python function to print cubes of first N natural numbers

def cube_N_num(n):
   if n > 0:
     cube_N_num(n - 1)
     print(n*n*n)
num8 = int(input("Enter N no. to print cubes of first N Natural no. :"))
cube_N_num(num8)
print()

#9. Write a recursive python function to print first N multiples of a given number.

def N_mul(n,m):
   i=1
   while i<=m:
     print(i*n,end=" " )
     i+=1
     print()
def f2(n,m):
     N_mul(n,m)

n=int(input("which number multiple you want: \n"))
m=int(input("how many times you wamt multiple of {} \n".format(n)))
f2(n,m) 
print()

#10. Write a recursive python function to print a number in reverse order

def rev(n, m):
    if n==0:
        return m
    else:
        return rev(n//10, m*10 + n%10)

number = int(input("Enter number: "))
reversed_number = rev(number,0)
print("Reverse of %d is %d" %(number, reversed_number))
print()