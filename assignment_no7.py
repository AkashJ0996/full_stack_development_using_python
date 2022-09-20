#1.Write a python script to display the number of days in a given month number.

m=int(input("enter month in number form :"))
match m in (1,3,5,7,8,10,12):
    case 1:
        print("Month of 31 days ")
match m in (4,6,9,11):
    case 1:
        print("Month of 30 days")
match m==2:
    case 1:
        print("Leap year = 29 days " if int(input("enter the year :")) % 4 == 0  else "year =  28 days")
print() 

"""2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""

print("enter two numbers")
a,b=eval(input()),eval(input())

print("tap 1 for addition")
print("tap 2 substraction")
print("tap 3 multiplication")
print("tap 4 division")

cal=eval(input("Enter your choice : "))
match cal :
    case 1:
        c=a+b
        print("sum is %0.2f"%c)
    case 2:
        c=a-b
        print("sub is %0.2f"%c)
    case 3:
        c=a*b
        print("mul is %0.2f "%c)
    case 4:
        c=a/b
        print("div is %0.2f"%c)
print()

"""3. Write a menu driven program with the following options:
        a. Check whether a given set of three numbers are lengths of an isosceles
           triangle or not
        b. Check whether a given set of three numbers are lengths of sides of a right
           angled triangle or not
        c. Check whether a given set of three numbers are equilateral triangle or not
        d. Exit."""

print("Enter three values of triangle length :")
x,y,z=eval(input()),eval(input()),eval(input())
        
print("1. isoseles tringle or not")
print("2. right angle triangle or not")
print("3. equilateral triangle or not") 
print("4. exit")
choice = int(input("Enter your choice : "))
match choice:
    case 1:
        if x==y or y==z or x==z:
            print("isosceles traingle")
        else:
            print("Not isosceles triangle")
    case 2:
        if x**2+y**2==z**2 :
            print("right andgle triangle")
        else:
            print("not right angle triangle")
    case 3:
        if x==y==z:
            print("equilateral triangle")
        else:
            print("not equilateal triangle")  

    case 4:
        exit()         
print()

"""4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

age = int(input("Enter your age please :"))
print("You entered :",age)

match age:
    case age if age<=10 :
            print("your age fits in KIDS category ")
    case age if age<20 :
            print("your age fits in TEEN AGER category ")
    case age if age<40 :
            print("your age fits in YOUNG category ")
    case age if age<60 :
            print("your age fits in EXPERIENCED PERSONS category ")
    case age if age>60 :
            print("your age fits in SENIOR CITIZENS category ")
    
print()

"""5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

num=int(input("enter a number : "))
print("you entered %d"%num)

match num :
    case num if num>0 and num % 2 == 0 :
        print (" Sourabh Shukla ")
    case num if num<0 and num % 2 == 1:
        print (" Pratik Jain ")
    case num if num>0 and num % 2 == 1:
        print (" Aditya Chaudhary ")

print()

"""6. write a python program to check whether a given string is a multiword string or single
word string using match case statement"""

x=input("Enter Something : ")
match x:
    case x if len(x)>1:
        print("multiword string")
    case x if len(x)==1:
        print("single word string")
print()

"""7. Write a python program to check whether a given number is positive, negative or
zero using match case statement"""

num = int(input("Enter a number : "))

match num :
    case num if num > 0:
        print("entered a positive no ")
    case num if num < 0:
        print("entered a negative no ")
    case num if num == 0 :               
        print("You enterd zero ")
print()

"""8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""
s1=input("enter 1 string : ")
s2=input("enter 2 string : ")
match s1,s2:
    case s1,s2 if s1==s2:
        print('identical')
    case s1,s2 if s1>s2:
        print('{} comes before {}'.format(s1,s2))
    case s1,s2 if s1<s2:
        print('{} comes after {}'.format(s2,s1))
print()

"""9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""

x=int(input("enter a year : "))
match x:
    case x if x%400!=0 and x%4==0:
        print("non century leap year ")
    case x if x%400==0:
        print("century leap year")
    case x if x%400!=0 and x%4!=0:
        print('non century non leap year')
    case x if x%400==0 and x%4!= 0  :
        print('century non leap year')
print()

"""10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""


colors=input("what is your fav colour : ")

match colors :
    case "yellow":
        print("monday")
    case "blue":
        print("tuesday")
    case "orange":
        print("wed")
    case "white":
        print("thurs")
    case "black":
        print("friday")
    case "red":
        print("saturday")
    case _:
        print("sunday")

print()
