# 1) Create a class cal1 that will calculate sum of three numbers. Create setdata() method which has three parameters that contain numbers. Create display() method that will calculate sum and display sum.

class Cal1:
    def setdata(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print("Sum = ",self.a + self.b + self.c)

calc = Cal1()
calc.setdata(4,5,6)
calc.display()

# 2) Create a class cal2 that will calculate area of a circle. Create setdata() method that should take radius from the user. Create area() method that will calculate area . Create display() method that will display area .

from math import *

class Cal2:
    def setdata(self,r):
        self.r = r

    def area(self):
        print("Area of Circle is = ",(pi*self.r*self.r))

calc = Cal2()
calc.setdata(7)
calc.area()

# 3) Create a class cal3 that will calculate simple interest. Create constructor method which has three parameters .Create calInterest() method that will calculate Interest . Create display() method that will display Interest.

from math import *

class Cal3:
    def calInterest(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def display(self):
        print("Simple Interest(S.I) = ",(self.p*self.r*self.t)) #P = Principle(4500), R = rate(9.5% = 0.095), T = time(6 yrs)

calc = Cal3()
calc.calInterest(4500,0.095,6)
calc.display()

# 4) Create a class cal4 that will calculate square of a number. Create setdata() method which has one parameters that contain number. Create display() method that will calculate sum.(Function should return value)

from math import *

class Cal2:
    def setdata(self,r):
        self.r = r

    def display(self):
        print("Area of Circle is = ",(self.r*self.r))

calc = Cal2()
calc.setdata(7)
calc.display()

# 5) Consider an employee class, which contains fields such as name and designation. And a subclass, which contains a field salary. Write a program for inheriting this relation.

class Employee:
    def info(self,name,designation):
        print("Employee's name: ",name)
        print("Employee's designation: ",designation)

class Sal(Employee):
    def salary(self,salary):
        print("Salary is: ",salary)

s = Sal()
s.info("Parth","Python Developer")
s.salary(50000)

# 6) Create a class cal5 that will calculate area of a rectangle. Create constructor method which has two parameters .Create calArea() method that will calculate area of a rectangle. Create display() method that will display area of a rectangle.

from math import *

class Cal5:
    def __init__(self,w,l):
        self.w = w
        self.l = l

    def calArea(self):
         return self.w*self.l

    def display(self):
        print("Area of Rectangle is: ",a)

calc = Cal5(7,8)
a = calc.calArea()
calc.display()

# 7) Create a class cal6 that will calculate area of a square. Create setdata() method that should take length from the user. Create area() method that will calculate area . Create display() method that will display area .

from math import *

class Cal6:
    def setdata(self):
        self.l = int(input("Entrer the length of square: "))

    def area(self):
         return self.l*self.l

    def display(self):
        print("Area of Square is: ",a)

calc = Cal6()
calc.setdata()
a = calc.area()
calc.display()

# 8) Write a program with use of inheritance: Define a class publisher that stores the name of the title. Derive two classes book and tape, which inherit publisher. Book class contains member data called page no and tape class contain time for playing. Define functions in the appropriate classes to get and print the details.

class Publisher:
    def title(self,name):
        print("Enter the name of book: ",name)

class Book(Publisher):
    def member(self,page_no):
        print("Enter the totla page number of book: ",page_no)

class Tape(Publisher):
    def time(self,play):
        print("Enter the total playing hour of tape: ",play)

b = Book()
t = Tape()
b.title("3 idiots")
b.member(630)
t.time("2.56 hrs")

# 9) Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge. Derive customer class form scheme and include cust_id, name and mobile_no data.Define necessary functions to read and display data.

class Scheme:
    def scheme_id(self,id):
        print("Enter your scheme id: ",id)

    def scheme_name(selfself,sname):
        print("Enter scheme name: ",sname)

    def outing_rate(self,rate):
        print("Enter rate of outgoing: ",rate)

    def message_charge(self,msg):
        print("Enter charge of messages: ",msg)

class Customer(Scheme):
    def cust_id(self,id1):
        print("Enter customer's id: ",id1)

    def cust_name(selfself,name):
        print("Enter customer's name: ",name)

    def mobile_no(self,num):
        print("Enter customer's mobile number: ",num)

cust = Customer()
cust.scheme_id(2)
cust.scheme_name("Binge all night with weekend data roll over at rs. 699")
cust.outing_rate(0)
cust.message_charge(0)
cust.cust_id(123)
cust.cust_name("Parth Shah")
cust.mobile_no(9658123785)

# 10) Create a arith class. The class should have a parameterized constructor and methods to add, subtract and multiply two numbers and to return the answers.

class Arith:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition of two number is: ",(self.a+self.b))

    def sub(self):
        print("Subtraction of two number is: ",(self.a-self.b))

    def mul(self):
        print("Multiplication of two number is: ",(self.a*self.b))

ar = Arith(45,10)
ar.add()
ar.sub()
ar.mul()
