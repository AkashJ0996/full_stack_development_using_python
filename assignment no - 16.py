"""1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple"""

var1=("java","python","SQL","c")
print(var1)
print()

#2. Write a python program to store only one item using tuple.

tup=("1item",)
print(tup)
print(type(tup))
print()

#3. Write a python program to reverse the tuple.

var1=("java","python","SQL","c")
print(var1[::-1])
print()

#4. Write a python program to Swap two tuples in Python.

tup1=(1,2,3,4,5)
tup2=(11,12,13,14,15)
tup1,tup2=tup2,tup1
print("after swaping tup1 :",tup1)
print("after swaping tup2 :",tup2)
print()

#5. Write a python program to check if all items in the tuple are the same.

tupn=(42,42,42,42)
print(set(tupn))#remove all  duplicate elements and represent it as one single element.
print("is tuple consist of same elements? :")
print(len(set(tupn))==1)#one single elements means length = 1)
print()
#count will return 4 and len will return 4
#both are equal hence tuple is identical.
print(tupn.count(tupn[0])==len(tupn))
print()

"""6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)"""

tuple1=(100, 200, 300, 400)
x1,x2,x3,x4=tuple1 #creating 4 different variables
print(x1,x2,x3,x4,sep="\n")
print()

"""7. Write a python program to copy elements 4 and 5 from the following tuple into a new
tuple. tuple1=(1,2,3,4,5,6)"""


tuple1=(1,2,3,4,5,6)
tuple2=(tuple1[3:5])
print(tuple1)
print(tuple2)
print(type(tuple2))
print()

"""8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))"""

t= (('a', 21),('b', 37),('c', 11), ('d',29))
print("my original tuple without sorted : ",t)
print("sorted tuple : ",sorted(t, key=lambda x: x[1]))
print()

"""9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))"""

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])
print()

"""10. Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]="i am changed"
print(tuple1)
print()