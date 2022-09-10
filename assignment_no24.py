#1. Write a python program to create a user class with 3 properties : name, age, email.
class user :
    #def __init__(self,name,age,email):

    name="_"
    age=0
    email="_"
    def show(name,age,email):
        print(name , age , email , sep=" : ")

user.show("akash",26,"abc@mail.com")
print()

#2. Write a python program to create a user class with a method to greet the user.
class user :
    def __init__(self,name):
        self.name=name
    def greetings(self):
        print("hey there it's nice to see you",self.name,"have a good day ...")
user007=user(input("enter your name :"))
user.greetings(user007)
print()

"""3. Write a python program to create 2 objects of the user class and assign different
values."""
class user :
    def __init__(self,name,gender):

        self.name=name
        self.gender=gender
        
    def show(self):
        print(self.name , self.gender ,sep=" : ")

user1=user("akash","M")
user2=user("alex","F")
user.show(user1)
user.show(user2)
print()

#4. Write a python program to init default values for user object using __init__ method.
class user :
    def __init__(self,name,age,email):

        self.name=name
        self.age=age
        self.email=email
    def show(self):
        print(self.name , self.age , self.email,sep=" : ")

user1=user("akash",26,"abj@mail.com")
user2=user("tomy",2,"tomythedog@mail.com")
print(user2.name)
user.show(user1)
user.show(user2)
print()

#5. Write a python program to delete the age property of the user.
class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Hello my name is ",self.name , "my age is " , self.age)

user1= user("Ramesh", 36)
user2= user("suresh", 39)

del user2.age

user.show(user1)
user.show(user2)#will throw erorr cause we deleted the age properties of user 2
print()

#6. Write a python program to create 3 user objects and find the youngest of all.
class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
       if user1.age<user2.age and user1.age<user3.age :
            print("user 1 is younger than user 2 and user 3")
       if user2.age<user1.age and user2.age<user3.age :
            print("user 2 is younger than user 1 and user 3")
       if user3.age<user1.age and user3.age<user2.age :
            print("user 3 is younger than user 1 and user 2")

user1= user("Ramesh", input("enter age for user1 :"))
user2= user("suresh", input("enter age for user2 :"))
user3= user("jayesh", input("enter age for user3 :"))
user.show(0)
print()

"""7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values)."""
class laptop:

    def __init__(self,brand,ram,cpu,hdd):
        self.brand = brand     
        self.ram = ram
        self.cpu = cpu      
        self.hdd = hdd

    def showConfig(self):
        print(self.brand , self.ram , self.cpu , self.hdd)

lapi1=laptop("hp",8,"i3",500)
lapi2=laptop("dell",4,"i5",467)
lapi3=laptop("lenovo",16,"i7","1TB")
lapi4=laptop("hp",16,"i7","2TB")

lapi1.showConfig()
lapi4.showConfig()
print()

"""8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size."""
class laptop:

    def __init__(self,brand,ram,cpu):
        self.brand = brand     
        self.ram = ram
        self.cpu = cpu      

    def showConfig(self):
        l1=[(lapi1.brand,lapi1.ram,lapi1.cpu),(lapi2.brand ,lapi2.ram,lapi2.cpu),(lapi3.brand,lapi3.ram,lapi3.cpu)]
        l1.sort()
        print(l1)
lapi1=laptop("hp",8,"i3")
lapi2=laptop("dell",4,"i5")
lapi3=laptop("lenovo",16,"i7")
laptop.showConfig(0)
print()

"""9. Write a python program to create a School class and 3 instance variables and 1 class
variable."""
class School:
    name_of_school="x.y.z school of arts"#class variable
    def __init__(self,name,rollno,div):
        self.name = name    
        self.rollno = rollno   #instance variable
        self.div = div
    def showOutput(self):
        print(self.name , self.rollno, self.div,sep=" : " )

print(School.name_of_school)
student1=School("ajay",8,'A')
student2=School("vijay",4,'B')
student3=School("sujay",16,'C')
student1.showOutput()
student2.showOutput()
student3.showOutput()
print()

"""10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values"""

class Employee:
    
    def __init__(self):
        self.empid = input("enter the empid :")    
        self.name =  input("enter the name :")
        self.salary = input("enter the salary :")
    
    def display(self):
        print("empid : ",self.empid ,"name :" ,self.name,"salary :",self.salary )

emp1=Employee()
emp2=Employee()
emp3=Employee()
emp1.display()
emp2.display()
emp3.display()

print()








 


