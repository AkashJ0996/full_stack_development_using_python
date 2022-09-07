#1. Write a python program to create a simple function which prints “MySirG” .
def name():
    
    print("MySirG")

name() 
print()

"""2. Write a python program to create a function which expects two arguments and print
them in the function body."""
def two_arguments(a,b):
   
   print("inside function body")
   print("a=",a,"b=",b)

two_arguments(5,10)
print()


"""3. Write a python program to create a function which expects an unknown number of
arguments."""
def unknown_arguments(*a):
   result=sum(a)
   
   print("Result of sum is :%d"%result)
   
unknown_arguments(10 , 20 , 30)
unknown_arguments(10 , 20 , 30 , 40 , 80 , 90 , 101)
unknown_arguments(20 , 30 , 40 , 50)
print()

#4. Write a python program to create a function which expects kwargs arguments.
def sum(**kwargs0):
   result=""
   print("Using **kwargs as a argument :")
   for arg in kwargs0.values():
      result += arg
   return result

print(sum(a="Ramesh ",b="and ",c="suresh ",d="both ",e="are ",f="cousins") )
print()

#5. Write a python program to create a function which expects a list as an argument.
def list_arguments(**list):
   
   for arg in list.values():
      print(arg)
   

list_arguments(l1=[1,2,3],l2=[5,6],l3=["apple","banana","cherry"])
print()

#6. Write a python program to create a function that finds a maximum of four numbers.
def max_num(data):
  largeno = data[0]

  for num in data:
    if num> largeno:
      largeno = num
  return largeno

print("Maximum no : ",max_num([0, 42, 28, 75]))
print()

#7. Write a python program to sum all the numbers in a list.
def sum_of_list_ele(l1):
    sum=0
    for i in range(len(l1)):
        sum = sum+l1[i]
    return sum

l1 = [10, 80, 90, 100]
print("Elements of List : ",l1)
print("sum of List Elements : ",sum_of_list_ele(l1))
print()

#8. Write a python program to multiply all the numbers in a list.
def multiplication_of_list(l2):
    sum=1
    for i in range(len(l2)):
        sum *= l2[i]
    return sum

l2 = [5, 10 , 15 , 20]
print("Elements of List : ",l2)
print("Multiplication of List Elements : ",multiplication_of_list(l2))
print()

"""9. Write a python program to create a function to check whether a number falls in a
given range."""
def weather_isin_range(n):
    if n in range(0,200):
        print( "%d is in the range"%int(n))
    else :
        print("%d is outside the given range."%int(n))

weather_isin_range(145)
weather_isin_range(55)
weather_isin_range(-2)
weather_isin_range(210)
print()

"""10. Write a python program to create a function to check whether a given number is even
or odd."""

def even_or_odd(n):
   
    if n%2==0  :
        print("%d is even number"%int(n))
    else :
        print("%d is odd number "%int(n))

even_or_odd(2)
even_or_odd(3)
even_or_odd(8)
even_or_odd(13)
print()