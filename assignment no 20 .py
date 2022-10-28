"""1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""

def funclist(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(funclist([1,2,3,3,3,3,4,5])) 
print()

"""2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""

def prime_or_not(num):
    if num == 1 :
        print("%d is not a prime number"%num)
    elif num == 2 :
         print("%d is a prime number"%num)
    else :
        for i in range(2,num):
            if (num % i) == 0:
                print("%d is not a prime number"%num)
                break 
        else:
                print("%d is a prime number"%num)
prime_or_not(int(input("Enter a num to cheak weather it is prime or not: ")))
print()

"""3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def is_e1(l):
    e1_num = []
    for n in l:
        if n % 2 == 0:
            e1_num.append(n)
    return e1_num
Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers present inside the list are : ",is_e1(Sample_List))
print()

"""4. Write a python program to create a function that checks whether a passed string is
palindrome or not."""

def is_pal(string):
	start_pos = 0
	end_pos = len(string) - 1
	
	while end_pos >= start_pos:
		if not string[start_pos] == string[end_pos]:
			return print("Entered string is not a PALINDROME :-(")
    
		start_pos += 1
		end_pos -= 1
	return print("You entered PALINDROME string")
is_pal(str(input("Enter a string : "))) 
print()

#5. Write a python program to create a function to find the Min of three numbers.

def min_num(a, b, c):
  
    if (a <= b) and (a <= c):
        minimum_no = a
  
    elif (b <= a) and (b <= c):
        minimum_no = b
    else:
        minimum_no = c
          
    print("min out of three numbers is :",minimum_no)
min_num(int(input("enter 1st num :")),int(input("enter 2nd num :")),int(input("enter 3rd num :")))
print()

"""6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""

def sq(li):
    sq_num = []
    for n in range(1,31):
            sq_num.append(n**2)
            n =+ 1
    return sq_num
sq_List = []
print("Even numbers present inside the list are : ",sq(sq_List))
print()

#7. Write a python program to access a function inside a function.

def month_salary(salary): 
    salary = salary
    print("monthly salary is",salary)
    def diwali_bonus(): 
        print("Salary with diwali bonus is ",salary+2000) 
    
    diwali_bonus()

month_salary(15000)
print()

"""8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters."""

def stringTesting(s):   
  count1=0
  count2=0
  for i in s:
      if(i.islower()):
            count1=count1+1
            
      elif(i.isupper()):
            count2=count2+1
  print("The number of lowercase characters is:",count1)
  print("The number of uppercase characters is:",count2)

stringTesting(str(input("Enter a string :")))
print()

"""9. Write a python program to create a function to check whether a string is a pangram
or not."""

  
def is_pangram(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if char not in str.lower():
           return print("string is not a pangram")
        
        return print("string is pangram")
is_pangram("The quick brown fox jumps over the lazy dog")
print()

"""10. Write a python program to create a function to check whether a string is an anagram
or not."""

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('top','pot'))
print(is_anagram('cat','rat'))
print()