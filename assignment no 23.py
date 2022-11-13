#1. Use iter and next method to access all the elements of a given set using while loop

set_a={2,3,4,5,6,7,8}
it=iter(set_a)
i=1
print("All the elements present inside the set is :")
while i<=len(set_a):
   print(next(it),end=" ")
   i+=1 

print()

#2. Create a generator to produce first n odd natural numbers

def odd_Gen(n):
    a = 1
    while n:
        yield a
        a += 2
        n -= 1

for odd in odd_Gen(int(input("Enter natural number to produce first n odd natural numbers :"))):
    print(odd, end=" ")

print()

#3. Create a generator to produce first n even natural numbers

def e1_Gen(n):
    a = 2
    while n:
        yield a
        a += 2
        n -= 1

for e in e1_Gen(int(input("Enter natural number to produce first n even natural numbers : "))):
    print(e, end=" ")

print()

#4. Create a generator to produce squares of first N natural numbers

def sq_Gen(n):
    a = 1
    while n:
        yield a**2
        a += 1
        n -= 1

for sq in sq_Gen(int(input("Enter n natural number to produce squares : "))):
    print(sq, end=" ")

print()

#5. Create a generator to produce first n terms of Fibonacci series

def N_fib(n):
    a = 0 
    y = 1
    while n:
        yield a
        a,y = y, a + y
        n -= 1

for f in N_fib(int(input("Enter number to produce first n terms of Fibonacci series : "))):
    print(f, end=" ")

print()

#6. Create a generator to produce first n prime numbers
def isprime(num):
    for i in range(2,num):
       if num % i==0:
            return False
    return True
def n_prime(n):
   num=2
   while n:
       if isprime(num):
            yield num
            n-=1
       num+=1
for x in n_prime(int(input("enter the n value : "))):
    print(x,end=" ")
print()

"""7. Create an endless iterator using generator method to produce terms of Fibonacci
series"""

def fib():
    a, b = 0, 1
    while True:
       yield a
       a, b = b, a + b

it = fib()
l1 = []

while True:
    x = int(input("Want to genrate another element[1 / 0]: "))
    if x == 1:
        n = next(it)
        l1.append(n)
        print(n)
    else:
        print()
        print(l1)
        break
print()

#8. Create an endless iterator using generator method to produce Prime numbers


def prime_Generator():
    x = 2
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1

it2 = prime_Generator()
l2 = []

while True:
    x = int(input("Want to generator another prime number[1 / 0]: "))
    if x == 1:
        n = next(it2)
        l2.append(n)
        print(n)
    else:
        print()
        print(l2)
        break
print()

"""9. Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides."""

def checkValidity(a, b, c):

    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True

print("enter the three number")
a,b,c=int(input()),int(input()),int(input())

if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid") 
print()

"""10. Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not."""

def HCF_co_prime(hcf_fun):
    def show(x, y):
        z = min(x, y)
        while z >= 1:
            if x % z == 0 and y % z == 0:
                if z == 1:
                    print("Co-prime numbers")
                    break
                else:
                    print("Not a co-prime")
                    break
            z -= 1
    return show

@HCF_co_prime
def HCF(a, b):
    h = min(a, b)
    while h >= 1:
        if a % h == 0  and  b % h == 0:
            print("HCF is:",h)
            break
        h -= 1

HCF(4, 8)