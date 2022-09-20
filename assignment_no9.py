#1. Write a python script to print MySirG N times on the screen

i=1
num=int(input('Enter the num : '))
while i<=num:
    print("MySirG")
    i+=1
print()

#2. Write a python script to print first N natural numbers

i=1
naturalNo=int(input('Enter the number to print the Natural num : '))
while i<=naturalNo:
    print(i,end=' ')
    i+=1
print()

#3. Write a python script to print first N natural numbers in reverse order

i=1
rev_nat=int(input("Enter the number to print the Natural num in rev. order : "))
while i<rev_nat:
    print(rev_nat-i,end =' ')
    i+=1
print()

#4. Write a python script to print first N odd natural numbers

i=1
Onum=int(input("Enter the number to print the odd Natural num : "))
while i<=Onum:
    if i%2!=0:
        print(i,end=' ')
    i+=1
print()

#5. Write a python script to print first N odd natural numbers in reverse order

i=1
Rev_Onum=int(input("Enter the number to print the odd Natural num in reverse order: "))
while i<Rev_Onum:
    if i%2!=0:
        print(Rev_Onum-i,end=' ')
    i+=1
print()

#6. Write a python script to print first N even natural numbers

i=1
e_1=int(input("Enter the number to print the even Natural num : "))
while i<e_1:
    if i%2==0:
        print(i,end=' ')
    i+=1
print()

#7. Write a python script to print first N even natural numbers in reverse order

i=1
Re_1=int(input("Enter the number to print the even Natural num in reverse order : "))
while i<Re_1:
    if i%2==1:
        print(Re_1-i,end=' ')
    i+=1
print()

#8. Write a python script to print squares of first N natural numbers

i=1
sq_no=int(input("Enter the number to get the squares : "))
while i<=sq_no:
    print(i**2,end =' ')
    i+=1
print()

#9. Write a python script to print cubes of first N natural numbers

i=1
cube=int(input("Enter the number to get the cubes : "))
while i<=cube:
    print(i**3, end =' ')                 
    i+=1
print()

#10. Write a python script to print first 10 multiples of N

i=1
num=int(input("Enter the number to get the multiples of N : "))
while i<=num:
    print(i*10,end=' ')
    i+=1
print()