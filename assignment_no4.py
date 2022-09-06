#1. Write a python script to take your name as input from the user and then print it.
x=(input("Enter your name:"))

print("Entered name is : ",x)
print()

#2. Write a python script to take input from the user. Input must be a number.
x=(int(input("Enter your age:")))

print("Age num is : ",x)
print()

"""3. Write a python script which takes two numbers from the user, then calculate their sum
and display the result."""

x=(int(input("Enter your age:")))
y=(int(input("Enter your year:")))

print("Sum of two num is equal to current year : ",x+y)
print()

#4. Write a python script which takes the radius from the user and display area of a circle.
r=(float(input("Enter radius of a circle:")))

a=3.14*r*r

print("Area of a circle is : ",a)
print()

#5. Write a python script to calculate the square of a number. Number is entered by the user.
num=(int(input("Enter a number:")))

sq=num**2

print("Square of a number is :",sq)
print()

#6. Write a python script to calculate the area of Triangle. Number is entered by the user.
  
side_x = (float(input('Enter first side: ')))  
side_y = (float(input('Enter second side: '))) 
side_z = (float(input('Enter third side: ')))  
  
base = (side_x + side_y + side_z) / 2  
  
 
area = (base*(base-side_x)*(base-side_y)*(base-side_z)) ** 0.5  
print('The area of the triangle is : %0.2f'%area)  
print()

#7. Write a python script to calculate average of three numbers, entered by the user
x=(int(input("Enter a numbers :")))
y=(int(input("Enter a numbers :")))
z=(int(input("Enter a numbers :")))

r=x+y+z/3
print("avg. of three numbers : ",r)
print()

#8. Write a python script to calculate simple interest
p=(float(input("Enter the amount of principle : ")))
r=(float(input("Enter the percent of  rate : ")))
t=(float(input("Enter the time : ")))

si=p*r*t/100

print("Calculated Simple Interest is :-",si,"Rs.")
print()

#9. Write a python script to calculate the volume of a cuboid.
l=(float(input("Enter the length : ")))
b=(float(input("Enter the breadth : ")))
h=(float(input("Enter the height: ")))

volume=(l * b * h)

print("the volume of a cuboid is :",volume)
print()

#10. Write a python script to calculate area of a rectangle
Rl=(float(input("Enter the length of a Rectangle : ")))
Rb=(float(input("Enter the breadth of a Rectangle : ")))
area=(Rl*Rb)

print("the area of a rectangle is :",area)
print()










