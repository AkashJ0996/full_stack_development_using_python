"""1.Write a python script to remove the last digit from a given number.(for example, if
user enters 2534 then your output should be 253)"""
x=(int(input("Enter the number : ")))
result= x // 10

print("the result is :%d "%result) 
print()

"""2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)"""
y=(int(input("Enter the number : ")))
result= y % 10

print("the result is :%d "%result) 
print()

#3. Write a python script to swap data of two variables.
x = (int(input('Enter value of x: ')))
y = (int(input('Enter value of y: ')))

temp = x
x = y
y = temp

print("The number after swapping x is : %d"%x)
print("The number after swapping y is : %d"%y)
print()

#4. Write a python script to find x power y, where values of x and y are given by user
x = (int(input('Enter value of x: ')))
y = (int(input('Enter value of y: ')))

result = x**y

print("x power of y  is : %d"%result)
print()

"""5. Write a python script which takes a three digit number from the user and displays
only its first digit."""
x=(int(input("Enter three digit number : ")))

result= x // 100

print("First digit of three digit no is :%d "%result) 
print()

"""6. Write a python script which takes a three digit number from the user and displays
only its middle digit."""
x=(int(input("Enter three digit number : ")))

result= x//10
middle_digit=result%10

print("Middle digit of three digit no is :%d " %middle_digit) 
print()

"""7. Write a python script which takes a three digit number from the user and displays
only its last digit."""
x=(int(input("Enter three digit number : ")))

result= x % 10

print("last digit of three digit no is :%d "%result) 
print()

#8. Write a python script to use IN operator to display the data present in the list
l1=["akash",25,25.0,"age",'number']

print(25.0 in l1 , 25 in l1 ,"number"in l1 ,sep="\n") 
print()

#9. Write a python script to use NOT IN operator to display the data not present in list
l2=["ramesh",253,25.0,"suresh",'number']

print(25.0 in l2 ,"number"in l2 ,sep="\n")
print()
print(256 not in l2 ,"yogesh" not in l2 ,13.5 not in l2 ,sep="\n")
print()
"""10. Write a python script to use IS operator to display if both variables are the same
object or not?"""

x="akash"
y=255

print(x is "akash")
print("prakash" is x)
print()
print(y is 255)
print(255 is y)
print()
print(x is y)
print()
