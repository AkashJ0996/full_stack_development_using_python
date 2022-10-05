#1. Write a Python script to create a list of first N natural numbers.

n=int(input("Enter a no to add it inside the list : "))
li=[]
for i in range(1,n+1):
    li.append(i)
print("You created a list of ",li,"Natural numbers")
print()

#2. Write a Python script to create a list of first N odd natural numbers.

n=int(input("Enter a no to add it inside the list : "))
l2=[]
for i in range (1,n+1,2):
    l2.append(i)
print("You created a list of ",l2," ODD Natural numbers")
print()

#3. Write a Python script to create a list of first N even natural numbers.

n=int(input("Enter a no to add it inside the list : "))
l3=[]
for i in range (2,n+1,2):
    l3.append(i)
print("You created a list of ",l3," EVEN Natural numbers")
print()

#4. Write a Python script to find the greatest number in a given list of numbers.

l4=[9,14,1,45,88,12,5,63,100,245,18,7]
print("The given list is :",l4)
greatest=max(l4)
print ("the greatest number in a list is : ",greatest)
print()

#5. Write a Python script to find the smallest number in a given list of numbers.

l5=[9,-14,1,45,88,12,0,63,100,-245,18,7]
print("The given list is :",l5)
Smallest=min(l5)
print ("the Smallest number in a list is : ",Smallest)
print()

#6. Write a Python script to calculate the sum of elements in a given list of numbers.

l6=[1,2,3,4,11,12,13,14,21,22,23,24]
print("The given list is :",l6)
addition=sum(l6)
print ("the sum of number in a list is : ",addition)
print()

#7. Write a Python script to remove all non int values from a list.

l7=[1,"ak",45,4,'t',"tomato",35,47]
print("The given list is :",l7)
newl7= [ i for i in l7 if type(i)==str ]
print ("After removing integer elements the present values in a list is : ",newl7)
print()

"""8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list."""

import collections
l8 = [10,20,10,10,20,50,40,60,60,60,60,20,20,40,40,50,50,30]
print("List : ",l8)
ctr = collections.Counter(l8)
print("Frequency of the elements in the List : ",ctr)
print()

"""9. Write a Python script to print indices of all occurrences of a given element in a given
list."""

l9 = [10,20,10,10,20,50,40,60,60,60,60,20,20,40,40,50,50,30]
print("List : ",l9)
lsize=len(l9)
for i in range(lsize):
    if (l9[i]==20):
        print(i,end=" ")
print()

#10. Write a python script to sort a list.

l10=[9,-14,1,45,88,12,0,63,100,-245,18,7]
print("The given list is :",l10)
addition=sorted(l10)
print ("the sum of number in a list is : ",addition)
print()