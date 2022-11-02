from turtledemo.chaos import h

import savings as savings

print("Hello World")
# this is just a comment
name = input('Please enter your name:')
print("Hello", name)
name = input("What is the name of your closest friend:")
# this is just another comment
# Variables such as username and name should be all lowercase

# Type of Variable Function
my_variable = "Ese"
print(type(my_variable))

# Built-in functions and strings
string_1 = 'Man'
string_2 = 'Kind'
string_3 = string_1 + string_2
string_4 = "be" + "very" + (string_2 * 5)
print(string_3)
print(len(string_3))  # string length
print(string_1 * 5)  # repeating strings
print(string_4)

# Splitting Strings
title = "Elon Musk is the richest man in the world "
print("source string:", title)
print("split using a space")
print(title.split(" "))
print("split using a comma")
print(title.split(","))

# Counting and replacing strings
my_string = "Count, the number of spaces in side this very long sentence right now"  # There are 12 spaces in here btw
print("Total number of spaces in the string:")
print(my_string.count(" "))

my_string = "Whats up!"
print(my_string)
print(my_string.replace("Whats up", "See you later"))

my_string = "Do you want some ice cream!"
print(my_string)
print(my_string.replace("Do you want some ice cream!", "I am very sorry we are all sold out"))

# Finding Sub Strings
string_1 = "Travis and Kanye are friends"
print(string_1.find("Kanye"))
print(string_1.find("Kylie"))  # test for absent/-1

# Converting other types into strings and Comparing strings
string_1 = "6ix" + str(9)
print(string_1)
print("Ese" == "Ese")  # true
print("Ese" == "Trevor")  # false
print("Ese" != "Trevor")  # true
print("Ese" == "ese")  # false .....extremely case sensitive

# Other strings


# Format{}
string_1 = 'Hello {}'
print(string_1.format('Hello'))

string_2 = '{} is {} years old'
Name = 'Ese'
Age = 20
print(string_2.format(Name, Age))

string_3 = "{1} and {2} are {0}"
print(string_3.format('friends', 'Travis', 'Ye'))

string_4 = "{artist} Bought {car} in {year}"
print(string_4.format(artist="Kanye west", car="Slr Mclaren", year="2009"))

string_5 = "{Celebrity} acquired {house} in {year}"
print(string_5.format(Celebrity="Kylie Jenner", house="Beverly Hills Mansion", year="2022"))

string_6 = "{Celebrity} Made {Dollars} in {year}"
print(string_6.format(Celebrity="Bhad Bhabie", Dollars="69 Million dollars", year="2022"))
# If,Else and elif statements

num = int(input('Enter a number:'))
if num < 0:
    print(num, 'is negative')

    print(num, 'squared is ', num * num)
else:
    print('its not negative')

Savings = float(input("enter how much you have in your savings:"))
if Savings == 0:
    print("Sorry no savings in your account")
elif Savings < 500:
    print('Well done')
elif Savings < 1000:
    print('Thats a healthy sum')
elif Savings < 10000:
    print('Welcome sir')
elif Savings < 100000:
    print('Good day sir')
else:
    print: 'thank you'

    # Nesting if statements

snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
if snowing:
    print('Put on boots')
    print('Time for some hot chocolate')
    print('bye')

    Heat = True
    temp = 30
if temp > 19:
    print('It is extremely hot')
if Heat:
    print('You might wanna go to the beach')
    print('Time for some cold showers')
    print('bye')

    # While and For Loop


#
# count = 0
# print('Starting')
# while count < 10:
#     print(count, '', end='')
# count += 1
# print('Done')
#
# print('Print out values in a range')
# for i in range(0, 5, 2):
#     print(i)
#     print('Done')
#
# strings with for loop
# print('Print out the letters in a string')
# for i in 'Hello world':
#     print(i)
#     print('Done')


# Break and Continue loop Statements
# print('only print code if all iterations completed')
# num = int(input('Enter a number to check for:'))
# for i in range(0, 19):
#     if i == num:
#         break
#     print(i)
#     print('Done')
#
#     for num in range(2, 10):
#         if num % 2 == 0:
#             print("Found an even number", num)
#         continue
#     print("Found an odd number", num)
#
#     num = int(input('Enter a number to check for:'))
#     for i in range(0, 6):
#         if i == num:
#             break
#         print(i, '', end='')
#     else:
#         print('All iterations successful')


# FFunctions
def animal(msg):
    print(msg)


animal('I hate cats')
animal('I love dogs')
animal('I like horses')


def square(n):
    return n * n


result = square(5)
print(result)


def operate(n, m):
    return n + m, n * m


a, b = operate(6, 3)
print(a)  # 'a' variable has n+m
print(b)  # 'b' variable has n*m

result = operate(6, 3)
print(result)


def welcome(message='Welcome Home buddy'):
    print(message)

    welcome()
    welcome('Nice to meet you')


#    Named arguments
def welcome(name, ask, message='welcome home buddy'):
    print(name, message, ask)


welcome('Ese', 'Nice to meet you', 'How are you?')


# Arbitrary and keyword Arguments
def find_space_diagonal(l, b, h):
    print(l,b,h)
    pass


def welcome(l=None, *nos):
    print(nos)
    print(nos[0])
    print(nos[2])

    # Space diagonal function call
    find_space_diagonal(l, b, h)

    welcome(1, 5, 9, 7)


def welcome(**nos):
    for i in nos.keys():
        print('arg:', i, 'has value:', nos[i])
        welcome(a=8, b=12, c=54)

        # Anonymous functions


add = lambda a, b: a + b
print(add(12, 5))

# python classes and types
print(type(7))
print(type(3.5))
print(type(True))
print(type('Trevor'))
print(type([3, 2, 4, 8]))


# Class Definition


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        p1 = Person('Ese', 20)
        p2 = Person('Trevor', 29)
        print(p1.name, 'is', p1.age)
        print(p1.name, 'is', p1.age)

        p1.name = 'Mike'
        p1.age = 68
        print(p1.name, 'is', p1.age)

        # Defining a default string representation


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('Happy Birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __str__(self):
                return 'Person[' + str(self.name) + '] is ' + str(self.age)


def calculate_pay(self, hours_worked):
    rate_of_pay = 9

    return hours_worked * rate_of_pay


p1 = Person('Trevor', 20)
print(p1)
p1.birthday()
print(p1)

pi = 22 / 7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2 * pi * radian) * height) + ((pi * radian ** 2) * 2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)

# for i in range(0, n):
#     print('Enter 1 for square')
#
#     print('Enter 2 for rectangle')
#
#     print('Enter 3 for cylinder')
#
#     choice = int(input('Enter your choice:'))
#
#     if (choice == 'Enter your choice:'):

# Python program to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

even_list = range(start, end + 1)[start % 2::2]

for num in even_list:
    print(num, end=" ")

    # Python program to print odd Numbers in given range
    lower = int(input("Enter the lower limit for the range:"))
    upper = int(input("Enter the upper limit for the range:"))
    for i in range(lower, upper + 1):
        if (i % 2 != 0):
            print(i)


# setter and getter methods

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age > 0 & new_age < 120:
            self._age = new_age

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


p = Person('Ese', 54)
print(p)
p.set_age(-1)
print(p)
p.set_age(25)
print(p)


# decorators
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method')
        if value > 0 & value < 120:
            self._age = value

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


p = Person('John', 54)
print(p)
print(p.age)
print(p.name)
p.age = 21
print(p)


# polymorphism
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
cat1.info()
dog1.info()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def nameinfo(self):
        print(f"I am a cat. My name is {self.name}.")

    def ageinfo(self):
        print(f"I am a cat. I am {self.age} years old.")


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

    def ageinfo(self):
        print(f"I am a Kitten. I am {self.age} years old.")


cat1 = Cat("Catty", 2.5)
kitten1 = Kitten("Kitty", 3)
cat1.nameinfo()
cat1.ageinfo()
kitten1.nameinfo()
kitten1.ageinfo()
