"""1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using list"""

List=[ "Java" , "Python", "SQL", "C" ]
print(List)

print()

#2. Write a python script to get the data type of a list.
List2=[ "Java" , 1996, 2.5 , 'C']
print(type(List2))
print(type(List2[2]))
print(type(List2[1]))
print(type(List2[3]))
print()
#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]
print(mylist[2])
print(mylist[-1])
print()

"""4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]"""

thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

thislist[1]="NoSQL"
thislist[3]="Flutter"
print("After change :",thislist)
print()

"""5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]"""

mylist =["Java", "SQL", "C", "Reactnative"]
print("Before adding at the end",mylist)
mylist.append("Python")
print("After adding at the end",mylist)
print()

"""6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )"""

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
print(firstlist,secondlist)
currentlist=firstlist+secondlist 
print("current list:",currentlist)
secondlist.append(firstlist[0])
secondlist.append(firstlist[1]) #adding each element
secondlist.append(firstlist[2])
print("After appending each elements one by one:",secondlist)
secondlist.append(firstlist) #this line will add whole list into updated list
print("After appending whole list :",secondlist)
print()

"""7. Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]"""

thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

for i in thislist:
    print(thislist.index(i),i)
print()

"""8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]"""

thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
print(thislist)
print(sorted(thislist))
print()

#9. Write a Python script to create a list of city names taken from the user.

list2_0=[]
add_ele=int(input("Enter no. of cities you want in the list : "))

for i in range(0,add_ele):
   new_ele=str(input())
   list2_0.append(new_ele)
print(list2_0)
print()

"""10. Write a Python script to create a list, where each element of the list is a digit of a
given number."""
print("Enter how many digits you want in the list : ")
num=int(input())
print("Enter digits")
list3=[]
i=0
while i<num:
    list3.append(int(input()))
    i+=1
print(list3)








