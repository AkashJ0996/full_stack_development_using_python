#1. Write a python program to store all the programming languages known to you using Set.
myset = {"c", "c++", "java","python","c#","javascript"}
print("Entered set : ",myset,"\n")

#2. Write a python program to store your own information {name, age, gender, so on..}
myset2 = set(("Akash", 26, "male","xyz@mail","Elektronics_Engg"))
print("Entered personal information  : ",myset2,"\n")

#3. Write a python script to get the data type of a Set.
print(type(myset))
print(type(myset2),"\n")

"""4. Write a Python script to find if “Python” is present in the set thisset = 
{"Java","Python", "Django"}"""

thisset = {"Java","Python", "Django"}
if "Python" in thisset:
    print("Yes, Python is present in this set","\n")

"""5. Write a python program to add items from another set to the current set. 
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}"""

thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print(thisset,secondset)
currentset=thisset.union(secondset)
print("After combining different sets current set is : ",currentset,"\n")

"""6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)

print(thisset,"\n")

"""7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}"""

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.remove("SQL")
print(thisset,"\n")

#8. Write a python program to delete the set completely.

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()
print(thisset,"\n")

"""9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", “SQL”}"""

thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Elements inside thisset are :")
for i in thisset :
    print(i)
print()

#10. Write a python program to find the maximum and minimum value in a set.

letset={25,85,45,65,5,3,2.2,2.5}
print("maximum element present inside set is :",max(letset))
print("minimum element present inside set is :",min(letset))