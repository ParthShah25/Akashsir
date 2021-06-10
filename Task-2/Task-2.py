# variable & types of variable

a = 10
b = 63
c = 45.55
d = "Parth"

print(a)
print("The value of B is: ",b)
print("The value of c is: ",c)
print("My Name is: ",d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# how to update the variables
d = "Shah"
print("The updated name of D is: ",d)

#datatypes in python
# 1)Number Datatypes
# type() --> gives us the variable types
# isinstance() --> gives us ans in true or false

a = 45
b = 46.5

print("a's type is: ",type(a))
print("b's type is: ",type(b))
print("b is complex number?: ",isinstance(46.5,complex))

c = 2 + 3j
print("c's type is: ",type(c),"c is complex number?: ",isinstance(2 + 3j,complex))

# 2)string datatypes
name = "Parth Shah"
print(name)
a = len(name)
print(a)
print(name[1])
print(name[1:7])
print(name[2:])
print(name[:10])

# 3)list datatypes - mutable
lst = [10,20,30,"Parth","Shah"]
print(lst)
a = len(lst)
print(a)
print(lst[1])
print(lst[1:6])
print(lst[2:])
print(lst[:5])
lst[2] = "SOU"
print(lst)

# 4) tuple datatypes - immutable
tup = (10,20,30,"Parth","Shah")
print(tup)
a = len(tup)
print(a)
print(tup[1])
print(tup[1:6])
print(tup[2:])
print(tup[:5])
# tup[2] = "SOU" give,s us error because tuple's value can't be changed
# print(tup)

# 5) dictionary datatypes 'key':'values'
dic = {"Name":"Parth","Gender":"Male","Intern at":"Akash Technolab"}
print(dic)
a = len(dic)
print(a)
print(dic["Name"])
print(dic["Gender"])
print(dic["Intern at"])
