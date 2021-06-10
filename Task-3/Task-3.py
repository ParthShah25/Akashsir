# 1.	Calculate average of 5 numbers.

a = int(input("Enter the value:"))
print(a)
b = int(input("Enter the value:"))
print(b)
c = int(input("Enter the value:"))
print(c)
d = int(input("Enter the value:"))
print(d)
e = int(input("Enter the value:"))
print(e)

avg = (a+b+c+d+e)/5
print(avg)

# 2.	Check whether number is even or odd.

a = int(input("Enter your number:"))

if a%2==0:
    print("The number is even..")

else:
    print("The number is odd..")

# 3.	Take a year and check whether it is leap year or not

yr = int(input("Enter any year: "))

if yr%4==0:
    print("The year is leap year")

else:
    print("The year is not leap year")

# 4.	Take a number and check whether it is zero, positive or negative.

a = int(input("Enter any number: "))

if a==0:
    print("The number is zero")

elif a>0:
    print("The number is positive")

else:
    print("The number is negative")

# 5.	Take 2 numbers and display greatest number. (Also check equal number condition)

a = int(input("Enter your First number: "))
b = int(input("Enter your Second number: "))

if a==b:
    print("The number is equal")

elif a>b:
    print("a is greater")

else:
    print("b is greater")

# 6.	Take a number and find factorial of that number.

a = int(input("Enter the number: "))

fact = 1

if a<0:
    print("factorial of this number is does not exist")

elif a==0:
    print("factorial of 0 is 1")

else:
    for i in range(1,a+1):
        fact = fact*i
    print("the factorial of",a,"is",fact)

# 7.	Write a program to swap 2 numbers using third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The value of a before swapping: ",a)
print("The value of b before swapping: ",b)

temp = a
a = b
b = temp

print("The value of a after swapping: ",a)
print("The value of b after swapping: ",b)

# 8.	Take 2 numbers and find smallest number.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

if a<b:
    print("a is smaller")

else:
    print("b is smaller")

# 9.	Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

a = int(input("Enter the number: "))

if a<100:
    print("number is less than 100")
    if a%2==0:
        print(a,"is even")

    else:
        print(a,"is odd")

else:
    print("number is not less than 100")

# 10.	Take a number to print the square of a number if it is less than 10.

a = int(input("Enter the number: "))

if a<10:
    print("The square of number which is less than 10 is: ",a*a)

else:
    pass

# 11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

a = int(input("Enter any number: "))

if a>=0:
    if a==0:
        print("The number is zero")

    else:
        print("The number is positive")

else:
    print("The number is negative")

# 12.	Take 3 numbers and find greatest number using nested IF….ELSE statement.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if a>b:
    if a>c:
        print("a is greater")

    else:
        print("c is greater")

elif b>c:
    print("b is greater")

else:
    print("c is greater")

# 13.	Take 3 numbers and find smallest number using logical operator.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if (a>b and a>c):
    print("a is greater")

elif (b>c):
    print("b is greater")

else:
    print("c is greater")

# 14.	Write a program to swap 2 numbers without taking third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The value of a before swapping: ",a)
print("The value of b before swapping: ",b)

a = a+b
b = a-b
a = a-b

print("The value of a after swapping: ",a)
print("The value of b after swapping: ",b)

# 15.	Take starting number and ending number from the user and print following series.
# Enter starting number : 30
# Enter ending number : 0

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range(a,b-1,-1):
    if i%3==0:
        print(i)
