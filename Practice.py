#First Python Program

print("Hello, World!")
print("I Like Pizza!")
print("It's really good!")

#variable - a container for a value (a piece of data)
#naming rules - can't start with a number, can't have spaces, can't use special characters
#best practice - use lowercase letters, use underscores to separate words

#Many Examples of Variables

favorite_food = "Pizza"
print(favorite_food)

favorite_color = "Blue"
print(favorite_color)

favorite_animal = "Cat"
print(favorite_animal)

favorite_number = 7
print(favorite_number)

favorite_book = "ONE PIECE"
print(favorite_book)

favorite_movie = "Inception"
print(favorite_movie)

favorite_song = "Frame of Mind"
print(favorite_song)

favorite_tv_show = "Stranger Things"
print(favorite_tv_show)

favorite_hobby = "Drawing"
print(favorite_hobby)

favorite_place = "Beach"
print(favorite_place)

favorite_season = "Winter"
print(favorite_season)

favorite_subject = "Math"
print(favorite_subject)

favorite_sport = "Formula 1"
print(favorite_sport)

favorite_game = "Chess"
print(favorite_game)

favorite_drink = "Red Bull"
print(favorite_drink)

favorite_candy = "Chocolate"
print(favorite_candy)

favorite_ice_cream = "Butterscotch"
print(favorite_ice_cream)

favorite_flower = "Red Spider Lily"
print(favorite_flower)

favorite_tree = "Oak"
print(favorite_tree)

favorite_bird = "Owl"
print(favorite_bird)

#Data Types - Different kinds of data that can be stored in variables
#Common Data Types - String, Integer, Float, Boolean
#String - A sequence of characters, enclosed in quotes
#Integer - A whole number, positive or negative, without decimals
#Float - A number that has a decimal place
#Boolean - A data type that can be either True or False

#Examples of Data Types

name = "Alice"  #String
age = 30        #Integer
height = 5.7    #Float
is_student = True  #Boolean
is_employed = False #Boolean
gpa = 3.8       #Float
num_siblings = 2 #Integer
has_pet = True   #Boolean
pet_name = "Buddy" #String

#Using Variables in Operations

print("My name is " + name)
print("I am " + str(age) + " years old.")
print("My height is " + str(height) + " feet.")
print("Am I a student? " + str(is_student))
print("Am I employed? " + str(is_employed))
print("My GPA is " + str(gpa))
print("I have " + str(num_siblings) + " siblings.")
print("Do I have a pet? " + str(has_pet))
print("My pet's name is " + pet_name)

#Changing Variable Values

age = 31
height = 5.8
is_student = False
is_employed = True
gpa = 3.9
num_siblings = 3
has_pet = False
pet_name = "Max"

print("Next year, I will be " + str(age) + " years old.")
print("My new height is " + str(height) + " feet.")
print("Am I a student now? " + str(is_student))
print("Am I employed now? " + str(is_employed))
print("My new GPA is " + str(gpa))
print("I now have " + str(num_siblings) + " siblings.")
print("Do I have a pet now? " + str(has_pet))
print("My new pet's name is " + pet_name)

#Above are examples of strings, integers, floats, and booleans, as well as how to change variable values and use them in operations.

#Format Strings

print(f"My name is {name}")
print(f"I am {age} years old.")
print(f"My height is {height} feet.")
print(f"Am I a student? {is_student}")
print(f"Am I employed? {is_employed}")
print(f"My GPA is {gpa}")
print(f"I have {num_siblings} siblings.")
print(f"Do I have a pet? {has_pet}")
print(f"My pet's name is {pet_name}")

#Using f-strings for formatted output
#f-strings are a way to embed expressions inside string literals, using curly braces {}
#They are prefixed with 'f' or 'F' before the opening quotation mark
#f-strings are available in Python 3.6 and later versions
#They provide a more readable and concise way to format strings compared to traditional methods like concatenation or the format() method
#They also support more complex expressions and can include function calls, arithmetic operations, and more

#typecasting
#Converting one data type to another

age_str = str(age)  #Integer to String
print(f"My age as a string is {age_str}")
height_int = int(height)  #Float to Integer (truncates decimal)
print(f"My height as an integer is {height_int}")
gpa_float = float(gpa)  #Integer to Float
print(f"My GPA as a float is {gpa_float}")
is_student_str = str(is_student)  #Boolean to String
print(f"Is student as a string: {is_student_str}")
is_employed_int = int(is_employed)  #Boolean to Integer (True=1, False=0)
print(f"Is employed as an integer: {is_employed_int}")
pet_name_list = list(pet_name)  #String to List of characters
print(f"My pet's name as a list of characters: {pet_name_list}")
num_siblings_str = str(num_siblings)  #Integer to String
print(f"Number of siblings as a string: {num_siblings_str}")
has_pet_int = int(has_pet)  #Boolean to Integer (True=1, False=0)
print(f"Has pet as an integer: {has_pet_int}")

#type() function - to check the data type of a variable

print(f"The data type of name is {type(name)}")
print(f"The data type of age is {type(age)}")
print(f"The data type of height is {type(height)}")
print(f"The data type of is_student is {type(is_student)}")
print(f"The data type of is_employed is {type(is_employed)}")
print(f"The data type of gpa is {type(gpa)}")
print(f"The data type of num_siblings is {type(num_siblings)}")
print(f"The data type of has_pet is {type(has_pet)}")
print(f"The data type of pet_name is {type(pet_name)}")

#User input (commented out to avoid interrupting the flow of the program)

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
user_age = input("Enter your age: ")
print(f"You are {user_age} years old.")
user_height = input("Enter your height in feet: ")
print(f"You are {user_height} feet tall.")
user_is_student = input("Are you a student? (yes/no): ")
user_is_student = user_is_student.lower() == 'yes'  #Convert to Boolean
print(f"Are you a student? {user_is_student}")
user_is_employed = input("Are you employed? (yes/no): ")
user_is_employed = user_is_employed.lower() == 'yes'  #Convert to Boolean
print(f"Are you employed? {user_is_employed}")
user_gpa = input("Enter your GPA: ")
print(f"Your GPA is {user_gpa}")
user_num_siblings = input("Enter number of siblings: ")
print(f"You have {user_num_siblings} siblings.")
user_has_pet = input("Do you have a pet? (yes/no): ")
user_has_pet = user_has_pet.lower() == 'yes'  #Convert to Boolean
print(f"Do you have a pet? {user_has_pet}")
user_pet_name = input("Enter your pet's name (if any): ")
print(f"Your pet's name is {user_pet_name}")

#The input() function allows you to take input from the user
#The input is always taken as a string, so you may need to convert it to the desired data type
#In this example, we convert 'yes'/'no' responses to boolean values
#The input section is commented out to avoid interrupting the flow of the program
#You can uncomment it to test user input functionality

#Arithmetic Operations

num1 = 10
num2 = 3
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {exponentiation}")

#Arithmetic operations include addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulus (%), and exponentiation (**)
#You can use these operations with integers and floats

#Math Funtions

import math
sqrt_num1 = math.sqrt(num1)
sqrt_num2 = math.sqrt(num2)
power_num1 = math.pow(num1, 2)
power_num2 = math.pow(num2, 3)
log_num1 = math.log(num1)
log_num2 = math.log(num2)
print(f"The square root of {num1} is {sqrt_num1}")
print(f"The square root of {num2} is {sqrt_num2}")
print(f"{num1} raised to the power of 2 is {power_num1}")
print(f"{num2} raised to the power of 3 is {power_num2}")
print(f"The natural logarithm of {num1} is {log_num1}")
print(f"The natural logarithm of {num2} is {log_num2}")

#The math module provides various mathematical functions
#You need to import the math module to use its functions
#Some common functions include sqrt() for square root, pow() for power, and log() for natural logarithm

#if, elif, else statements

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

#The if statement is used to make decisions in your code
#The elif (else if) statement is used to check multiple conditions
#The else statement is used to execute code when none of the previous conditions are met

#logical operators

is_student = True #Boolean variable
is_employed = False #Boolean variable
if is_student and not is_employed:
    print("You are a student and not employed.")
elif is_student and is_employed:
    print("You are a student and employed.")
elif not is_student and is_employed:
    print("You are not a student but employed.")
else:
    print("You are neither a student nor employed.")

#Logical operators include and, or, and not
#They are used to combine multiple conditions in if statements
#The and operator returns True if both conditions are True
#The or operator returns True if at least one condition is True
#The not operator negates the condition, returning True if the condition is False and vice versa
#The input section is included here to demonstrate the use of if, elif, else statements and logical operators
#You can uncomment it to test the functionality

#String Methods

user_name = input("Enter your name: ")
print(f"Your name is {user_name}")
print(f"Your name in uppercase is {user_name.upper()}")
print(f"Your name in lowercase is {user_name.lower()}")
print(f"The length of your name is {len(user_name)} characters.")
print(f"Does your name start with 'A'? {user_name.startswith('A')}")
print(f"Does your name end with 'e'? {user_name.endswith('e')}")
print(f"Is your name alphabetic? {user_name.isalpha()}")
print(f"Is your name alphanumeric? {user_name.isalnum()}")
print(f"Your name with leading and trailing spaces removed: '{user_name.strip()}'")

#String methods are built-in functions that can be used to manipulate strings
#Some common string methods include upper(), lower(), len(), startswith(), endswith(), isalpha(), isalnum(), and strip()
#The input section is included here to demonstrate the use of string methods

#string indexing and slicing

first_character = user_name[0]
last_character = user_name[-1]
substring = user_name[1:4]
print(f"The first character of your name is: {first_character}")
print(f"The last character of your name is: {last_character}")
print(f"A substring of your name is: {substring}")

#String indexing allows you to access individual characters in a string using their position (index)
#String slicing allows you to extract a substring from a string using a range of indices
#Indexing starts at 0 for the first character, 1 for the second character, and so on
#Negative indexing starts at -1 for the last character, -2 for the second last character, and so on

#while loops

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  #Increment count by 1
print("Finished counting!")

#The while loop is used to execute a block of code repeatedly as long as a condition is True
#Make sure to include a way to break out of the loop, otherwise it will run indefinitely
#In this example, the loop will run as long as count is less than 5
#The count variable is incremented by 1 in each iteration to eventually break the loop
#The loop will print the value of count in each iteration and a message when finished

#for loops

for i in range(5):
    print(f"Iteration {i}")
print("Finished iterations!")

#The for loop is used to iterate over a sequence (like a list, tuple, or string) or a range of numbers
#The range() function generates a sequence of numbers, which can be used in a for loop
#In this example, the loop will run 5 times, with i taking values from 0 to 4
#The loop will print the value of i in each iteration and a message when finished
#You can also iterate over other sequences, like lists or strings

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
print("Finished listing fruits!")

#In this example, the loop iterates over a list of fruits
#The variable fruit takes the value of each item in the list in each iteration
#The loop will print a message for each fruit in the list and a message when finished
#You can use for loops to iterate over any iterable object, such as lists, tuples, strings, and more

#nested loops

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
print("Finished nested loops!")

#Nested loops are loops inside other loops
#The inner loop will run completely for each iteration of the outer loop
#In this example, the outer loop runs 3 times (i = 0, 1, 2) and for each iteration of the outer loop, the inner loop runs 2 times (j = 0, 1)
#The loop will print the values of i and j in each iteration and a message when finished

#break and continue statements
for i in range(10):
    if i == 5:
        print("Breaking the loop at i = 5")
        break  #Exit the loop when i is 5
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue  #Skip the rest of the loop for even numbers
    print(f"Processing number: {i}")
print("Finished loop with break and continue!")

#The break statement is used to exit a loop prematurely when a certain condition is met
#The continue statement is used to skip the current iteration of a loop and move to the next iteration
#In this example, the loop will break when i is 5 and skip even numbers
#The loop will print messages for odd numbers and a message when finished

#sets lists and tuples

#List - An ordered, mutable collection of items, defined using square brackets []

#Tuple - An ordered, immutable collection of items, defined using parentheses ()

#Set - An unordered, mutable collection of unique items, defined using curly braces {}

#List Example

fruits = ["apple", "banana", "cherry"]
print("Fruits List:")
for fruit in fruits:
    print(f"- {fruit}")
fruits.append("orange")  #Add an item to the list
print("Updated Fruits List:")
for fruit in fruits:
    print(f"- {fruit}")

#Tuple Example

coordinates = (10, 20)
print("Coordinates Tuple:")
print(f"- X: {coordinates[0]}")
print(f"- Y: {coordinates[1]}")

#Sets Example

unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers Set:")
for num in unique_numbers:
    print(f"- {num}")
unique_numbers.add(6)  #Add an item to the set
print("Updated Unique Numbers Set:")
for num in unique_numbers:
    print(f"- {num}")

#Lists are mutable, meaning you can change their contents (add, remove, modify items)
#Tuples are immutable, meaning once they are created, their contents cannot be changed
#Sets are mutable, but they only allow unique items (no duplicates)
#You can use loops to iterate over lists, tuples, and sets
#You can use various methods to manipulate lists and sets (e.g., append(), remove(), add())
#You can access items in lists and tuples using indexing
#You can convert between these data types using functions like list(), tuple(), and set()
#The examples above demonstrate the use of lists, tuples, and sets in Python

#Dictionaries

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person Dictionary:")
for key, value in person.items():
    print(f"- {key}: {value}")
person["age"] = 31  #Update an item in the dictionary
person["job"] = "Engineer"  #Add a new item to the dictionary
print("Updated Person Dictionary:")
for key, value in person.items():
    print(f"- {key}: {value}")

#Dictionary - An unordered, mutable collection of key-value pairs, defined using curly braces {}
#Dictionaries are mutable, meaning you can change their contents (add, remove, modify items)
#You can use loops to iterate over dictionaries using the items() method to get key-value pairs
#You can access items in dictionaries using their keys
#You can use various methods to manipulate dictionaries (e.g., keys(), values(), items())
#You can convert between dictionaries and other data types using functions like dict(), list(), and tuple
#The example above demonstrates the use of dictionaries in Python

#Functions

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum of 5 and 3 is {result}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
fact_5 = factorial(5)
print(f"The factorial of 5 is {fact_5}")

#Functions are reusable blocks of code that perform a specific task
#You define a function using the def keyword, followed by the function name and parentheses
#You can pass parameters to functions and return values using the return statement
#You can call a function by using its name followed by parentheses, passing any required arguments
#Functions help to organize code, make it more readable, and avoid repetition
#The examples above demonstrate the use of functions in Python, including a simple greeting function, an addition function, and a recursive factorial function
#You can define functions with default parameters, variable-length arguments, and keyword arguments for more flexibility
#You can also use lambda functions for small, anonymous functions
#You can document your functions using docstrings to explain their purpose and usage
#You can use built-in functions and create your own custom functions to suit your needs

#file handling (Txt,Binary,Csv)

#Text File Example

with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a text file.\n")
    file.write("File handling in Python is easy!\n")
with open("example.txt", "r") as file:
    content = file.read()
    print("Text File Content:")
    print(content)

#Binary File Example

data = bytearray([120, 3, 255, 0, 100])
with open("example.bin", "wb") as file:
    file.write(data)
with open("example.bin", "rb") as file:
    content = file.read()
    print("Binary File Content:")
    print(content)

#CSV File Example

import csv
with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV File Content:")
    for row in reader:
        print(row)

#File handling allows you to read from and write to files on your computer
#You can open a file using the open() function, specifying the file name and mode (e.g., "r" for read, "w" for write, "a" for append, "rb" for read binary, "wb" for write binary)
#You can use the with statement to automatically close the file after the block of code is executed
#You can read the content of a file using methods like read(), readline(), and readlines()
#You can write content to a file using methods like write() and writelines()
#You can handle different file types, such as text files, binary files, and CSV files
#The examples above demonstrate file handling in Python, including reading and writing text files, binary files, and CSV files
#Make sure to handle exceptions and errors when working with files, such as file not found or permission denied
#You can also use libraries like pandas for more advanced file handling, especially with CSV and Excel files
#Remember to clean up any files created during testing if necessary

#stack

stack = []

# Push elements onto the stack

stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack

top_element = stack.pop()
print(f"Popped element: {top_element}")
print(f"Current stack: {stack}")

# Peek at the top element without removing it

if stack:
    top_element = stack[-1]
    print(f"Top element: {top_element}")
else:
    print("Stack is empty")

# Check if the stack is empty

is_empty = len(stack) == 0
print(f"Is the stack empty? {is_empty}")

# Stack is a linear data structure that follows the Last In First Out (LIFO) principle
# You can use a list to implement a stack in Python
# The append() method is used to push elements onto the stack
# The pop() method is used to remove and return the top element from the stack
# You can access the top element of the stack using indexing (stack[-1])
# You can check if the stack is empty by checking the length of the list
# The example above demonstrates basic stack operations such as push, pop, peek, and checking if the stack is empty

#End of file.