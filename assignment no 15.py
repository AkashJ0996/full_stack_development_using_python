#1. Write a python script to create a String in 3 different possible ways
#1.
string="iNeuron"
print(string)
print()
string2='iNeuron'
print(string2)
print()
#2.
string3='''hey the best web development program'''
print(string3)
print()
string3="""is created by iNeuron
with Affordable prices.."""
print(string3)
print()
#3.
string4=str(543)#we add int value in str func. but it will produce as a string.
print(string4)
print(type(string4))
print()

"""2. Write a python script to Get the characters from the start to position 5 (Given String
“iNeuron” using the slice syntax)"""

s="iNeuron"
print(s[0:5])
print() 

print(s[-7:-2])
print()

"""3. Write a python script to Get the characters from position 2 to position 5 (Given String
“Hello Learners” using the slice syntax)"""

str2="Hello Learners"
print(str2[2:5])
print() 
print(str2[-12:-9])
print() 

"""4. Write a python script to demonstrate String Concatenation adding space in between (
Given Strings a=”Learning” b=”Python” )"""

a="Learning"
b="Python"
print(a+b) #concatenation 
print(a+" "+b)#adding space 
print()

"""5. Write a python script to get the count of total number of characters in String a=
“iNeuron”"""

a="iNeuron"
print("length of char in a is:", len(a))

count=0
for i in a:
    count=count+1
print("no of char in string a is :",count)

a2="iNNNNeuron"
print(a2.count("N"))
print()

#6. Write a python script to reverse a String. (“iNeuron”)

str3="iNeuron"
print(str3[::-1])
print()

#7. Write a python script to determine whether a string contains a specific substring.

a1="iNeuron" 
a2="Neuro"               
if a2 in a1:
    print("substring found")
else:
    print("not found")
print()

#8. Write a python script to check if a string contains only numbers.

num="123456"
print(num.isnumeric())
print(num.isdigit())
print(num.isalpha())
print()

#9. Write a python script to check if a string contains only characters of the alphabet.

num="1a2b3c456"
print(num.isalpha())
print()
char="abcdefg"
if char.isalpha()==True :
        print("yes str contains only alphabet")
else : 
        print("no it does contain numbers also")
print()
stri="akash"
print(stri.isalpha())
print(stri.isnumeric())
print()

#10. Write a python script to convert an integer to a string.

a=14
print(a)
print(type(a))
print()

a=str(14)
print(a)
print(type(a))
print()

a=int(input("enter a num :"))
print(type(a))
a=str(a)
print(type(a))
print()