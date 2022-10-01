#1. Write a python script to print the first 10 multiples of 5.

for i in range(1,11) :
    print(5*i)
print()   

#2. Write a python script to print first 10 multiples of N

n=int(input("enter a num : "))
for i in range(1,11) :
    print(n*i)
print() 

#3. Write a python script to print first M multiples of N.
M=int(input("enter a M num : "))
N=int(input("enter a N num : "))
for i in range(1,M+1) :
    print(N*i)
print() 

#4. Write a python script to print the first 10 multiples of N in reverse order.

n=int(input("enter a num : "))
for i in range(10,0,-1):
    print(i*n)
print()

#5. Write a python script to print table of user’s choice

n=int(input("enter a num : "))
for i in range(1,11) :
    print(n ,"x", i ,"=", n*i)
print()

#6. Write a python script to print first N even natural numbers.

n=int(input("enter a num : "))
for i in range(2,n*2+1,2) :
    print(i)
print()

#7. Write a python script to print first N odd natural numbers


n=int(input("enter a num : "))
for i in range(1,n*2+1,2) :
    print(i)
print()

#8. Write a python script to print squares of first N natural numbers.

n=int(input("enter a num : "))
for i in range(1,n+1) :
    print(i**2)
print()

#9. Write a python script to print cubes of first N natural numbers.

n=int(input("enter a num : "))
for i in range(1,n+1) :
    print(i**3)
print()

"""10. Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45"""

for n in range (15,45):  
    if n > 1:  
        for i in range (2, n):  
            if (n % i) == 0:  
                break  
        else:  
            print (n)  
print()



