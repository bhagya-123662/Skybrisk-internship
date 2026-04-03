#---------------------------week-1--------------------------------#

#introduction to python
#Python Variables 
#Python variables are used to store data values in a program. 
# A variable acts like a container that holds information which can be used and 
# changed during program execution.
# Rules for Naming Variables:
# Must start with a letter or underscore (_).
# Cannot start with a number.
# Can contain letters, numbers, and underscores.
# Variable names are case-sensitive (age and Age are different).

#example
age = 20
Age = 25
print(age)  # 20
print(Age)  # 25

# Common Data Types Stored in Variables:
# int – integers (10, 25)
# float – decimal numbers (3.5)
# str – text ("Hello")
# bool – True or False

# Operators in Python

# Operators are symbols used to perform operations on variables and values in Python.

# Types of Operators

# Arithmetic Operators: + , - , * , / , % , ** , //
# Comparison Operators: == , != , > , < , >= , <=
# Logical Operators: and , or , not
# Assignment Operators: = , += , -= , *=
# Operators help perform calculations, comparisons, and logical decisions in programs.

# Input and Output in Python
# Input and output are used to interact with the user.

# Input: The input() function is used to take input from the user.
# Output: The print() function is used to display output
# Example:
# name = input("Enter your name: ")
# print("Hello", name)

# Conditional Statements

# Conditional statements are used to make decisions in a program based on conditions.

# Common conditional statements:

# if
# if-else
# if-elif-else
    
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

#     Loops in Python

# Loops are used to repeat a block of code multiple times.

# Types of loops:

# for loop – used when the number of iterations is known.
# while loop – used when the condition controls the repetition.

# Example:
for i in range(5):
    print(i)

#Output:

0
1
2
3
4

# Summary:

# In Python, several basic concepts are used to build programs.

# Operators are symbols used to perform operations on variables and values, such as arithmetic, comparison, and logical operations.
# Input and Output allow interaction between the user and the program. The input() function is used to take input from the user, and the print() function is used to display results.
# Conditional Statements are used to make decisions in a program. Statements like if, if-else, and if-elif-else execute different blocks of code based on conditions.
# Loops are used to repeat a block of code multiple times. Common loops include for and while.

# Overall, these concepts help in performing calculations, taking user input, making decisions, and repeating tasks, which are essential for writing efficient Python programs.

#hands on

#Program to Find Factorial of a Number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


#Program to Print Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#Basic Data Processing Script
# Input data
numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# Data processing
total = sum(numbers)
average = total / n
maximum = max(numbers)
minimum = min(numbers)

# Output results
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)


#----------------------------------week-2-----------------------------#
#Data structures and functions
# Lists
# A list in Python is a flexible data structure used to store and manage multiple values in a single variable, making programs easier and more efficient to write.

# Characteristics of Lists
# Ordered – Items have a fixed order.
# Mutable – List elements can be changed after creation.
# Allows duplicates – Same value can appear multiple times.
# Stores different data types.

# Example:
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
print(fruits[1])   # banana

# Common List Operations

# Add element
fruits.append("orange")

# Remove element
fruits.remove("banana")

# Length of list
len(fruits)

# Tuples
# In Python, a tuple is a collection of items stored in a single variable, similar to a list. However, the main difference is that tuples are immutable, meaning their elements cannot be changed after creation.

# Tuple elements are accessed using index numbers starting from 0.
fruits = ("apple", "banana", "mango")
print(fruits[0])   # apple
print(fruits[1])   # banana

# Dictionaries 
# In Python, a dictionary is a data structure used to store data in key–value pairs. Each value in the dictionary is accessed using its key.

# Characteristics of Dictionaries
# Store data in key : value pairs
# Keys must be unique
# Values can be duplicated
# Mutable – values can be changed after creation
# Can store different data types

# Example Program

student = {
    "name": "Anita",
    "marks": 85
}

print("Name:", student["name"])
print("Marks:", student["marks"])

# Sets
# In Python, a set is a collection of unique and unordered elements. Sets are mainly used to store distinct values and perform mathematical set operations.

# Example:
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "mango"}

# Characteristics of Sets
# Unordered – items do not have a fixed position.
# No duplicate values – duplicate elements are automatically removed.
# Mutable – elements can be added or removed.
# Can store different data types.

# Functions

# In Python, a function is a block of reusable code that performs a specific task. Functions help make programs organized, reusable, and easier to understand.
# Defining a Function
# Functions are defined using the def keyword.

# Example:
def greet():
    print("Hello, welcome!")
# Calling a Function

# To use a function, we call it by its name.

# Example:
greet()

# Function with Parameters
# Functions can take inputs (parameters).

# Example:
def add(a, b):
    result = a + b
    print("Sum =", result)

# add(5, 3)

# Function with Return Value
# Functions can return values using return.

# Example:
def multiply(a, b):
    return a * b

result = multiply(4, 3)
print(result)

# Advantages of Functions
# Code reusability
# Better program organization
# Reduces repetition
# Improves readability

# Lambda Functions
# In Python, a lambda function is a small anonymous (nameless) function used to perform simple operations. It is written in one line using the keyword lambda.

# Syntax
# lambda arguments : expression

# Example
add = lambda a, b: a + b
print(add(5, 3))

# Output:8

# Example 2
square = lambda x: x * x
print(square(4))

# Output:16

# Characteristics of Lambda Functions
# Anonymous – no function name.
# Single expression only.
# Used for short and simple operations.
# Often used with functions like map(), filter(), and sorted().

# Recursion
# In Python, recursion is a technique where a function calls itself to solve a problem. It is commonly used to solve problems that can be broken down into smaller similar subproblems.

# Structure of Recursion
# A recursive function has two important parts:

# Base Case – condition where the function stops calling itself.
# Recursive Case – the function calls itself with a smaller input.

# Example: Factorial Using Recursion
def factorial(n):
    if n == 1:          # Base case
        return 1
    else:
        return n * factorial(n-1)   # Recursive call

# num = 5
# print("Factorial =", factorial(num))

# Output
# Factorial = 120

# Advantages
# Makes code shorter and easier to understand for some problems.
# Useful for problems like factorial, Fibonacci series, and tree traversal.
    
# List Comprehension
# In Python, list comprehension is a short and concise way to create lists using a single line of code. It helps make the code simpler and more readable.

# Syntax
# [expression for item in iterable if condition]
# Example 1: Creating a List
numbers = [x for x in range(5)]
print(numbers)

# Output
# [0, 1, 2, 3, 4]

# Example 2: Squares of Numbers
squares = [x*x for x in range(1,6)]
print(squares)

# Output
# [1, 4, 9, 16, 25]

# Example 3: List with Condition
even = [x for x in range(10) if x % 2 == 0]
print(even)

# Output
# [0, 2, 4, 6, 8]

# Advantages
# Shorter code
# Easy to read
# Faster list creation

# hands-on:
# Data structures like lists and dictionaries are used to store data. 
# Functions can be written to transform (modify or process) the data using loops instead of list comprehension.

# Example 1: Square Numbers in a List
def square_numbers(numbers):
    result = []
    
    for num in numbers:
        result.append(num * num)
    
    return result

data = [1, 2, 3, 4, 5]
print(square_numbers(data))

# Output
# [1, 4, 9, 16, 25]

# Example 2: Filter Even Numbers
def filter_even(numbers):
    result = []
    
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    
    return result

data = [1, 2, 3, 4, 5, 6]
print(filter_even(data))

# Output
# [2, 4, 6]

# Example 3: Transform Dictionary Values
def increase_marks(students):
    for key in students:
        students[key] = students[key] + 5
    
    return students

marks = {"Asha": 80, "Ravi": 75, "Kiran": 90}

print(increase_marks(marks))

# Output
# {'Asha': 85, 'Ravi': 80, 'Kiran': 95}

# Summary:
# Data transformations can be performed by writing functions and using 
# loops to modify lists or dictionaries, 
# which helps in processing and organizing data step by step.

# client project:
# A data processing script collects data, processes it, and displays the results.
# Input data
numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Processing data
total = 0
for num in numbers:
    total = total + num

average = total / n

# Output results
print("Numbers entered:", numbers)
print("Sum of numbers:", total)
print("Average:", average)

#--------------------week 3------------------------#
#NumPy and Pandas for Data Manipulation
# NumPy Arrays:
# a NumPy array is a powerful data structure used to store and process large sets of numerical data efficiently. It is faster and more memory-efficient than regular Python lists for mathematical operations.
    
# Creating a NumPy Array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Types of NumPy Arrays:
# 1. One-Dimensional Array:
arr = np.array([10, 20, 30])

# 2. Two-Dimensional Array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# # Basic Operations on NumPy Arrays

# Addition
arr = np.array([1, 2, 3])
print(arr + 5)

# # Multiplication
print(arr * 2)

# # Finding Mean
print(np.mean(arr))

# NumPy Broadcasting :
# In NumPy used with Python, broadcasting is a technique that allows arrays of different shapes or sizes to perform mathematical operations together.

# Example: Broadcasting Between Arrays
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([10])

result = arr1 + arr2
print(result)

# Pandas DataFrame 
# In pandas used with Python, a DataFrame is a two-dimensional data structure used to store data in rows and columns, similar to a spreadsheet or table.
# It is widely used for data analysis, data processing, and data manipulation.

# Creating a DataFrame
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Kiran"],
    "Age": [20, 21, 19],
    "Marks": [85, 78, 90]
}

df = pd.DataFrame(data)

print(df)

# Output
#     Name  Age  Marks
# 0   Asha   20     85
# 1   Ravi   21     78
# 2  Kiran   19     90


# Pandas Series 
# In pandas used with Python, a Series is a one-dimensional data structure that stores data in a single column with labels called indexes.
# It is similar to a column in a table or a list with labels.

# Indexing in Python Data Structures 
# In Python, indexing is the process of accessing individual elements of a data structure using their position (index number). Indexing is commonly used in lists, tuples, strings, and arrays.

# Example with a List
numbers = [10, 20, 30, 40]

print(numbers[0])  # first element
print(numbers[2])  # third element


#Negative Indexing
numbers = [10, 20, 30, 40]

print(numbers[-1])  # last element
print(numbers[-2])  # second last element

# Output
# 40
# 30

# Data Grouping 
# In pandas used with Python, data grouping is the process of grouping data based on one or more columns and then performing operations like sum, mean, count, or average on those groups.
# This is done using the groupby() function.
# Example:
import pandas as pd
data = {
    "Department": ["IT", "HR", "IT", "HR", "Finance"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)
result = df.groupby("Department")["Salary"].mean()
print(result)

# Output
# Department
# Finance    55000
# HR         42500
# IT         55000

# Performing Operations with NumPy and Manipulating Datasets with Pandas
# NumPy is mainly used for numerical calculations, while Pandas is used for handling and analyzing datasets.

# Operations with NumPy
# NumPy helps perform fast mathematical operations on arrays.

import numpy as np
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))

#Output
# Array: [10 20 30 40]
# Sum: 100
# Mean: 25.0
# Maximum: 40

# Manipulating Dataset with Pandas
# Pandas helps create, analyze, and manipulate tabular datasets.
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Kiran"],
    "Marks": [85, 78, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())

# Output
# Dataset:
#     Name  Marks
# 0   Asha     85
# 1   Ravi     78
# 2  Kiran     90
# Average Marks: 84.33
# Maximum Marks: 90

# Cleaning and Aggregating a Dataset using pandas 

# In Python, data cleaning means removing errors, missing values, or duplicates from a dataset, while aggregation means summarizing data using operations like sum, average, or count.

# Example Dataset Cleaning and Aggregation
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Asha", "Kiran", None],
    "Marks": [85, 78, 85, 90, 70]
}

df = pd.DataFrame(data)

# Data Cleaning
df = df.drop_duplicates()     # remove duplicate rows
df = df.dropna()              # remove missing values

# Data Aggregation
avg_marks = df["Marks"].mean()
total_marks = df["Marks"].sum()

print("Cleaned Dataset:")
print(df)

print("Average Marks:", avg_marks)
print("Total Marks:", total_marks)
# Output
# Cleaned Dataset:
#     Name  Marks
# 0   Asha     85
# 1   Ravi     78
# 3  Kiran     90

# Average Marks: 84.33
# Total Marks: 253

# #------------------------------week-4--------------------------#
# Matplotlib and Seaborn

# Both Matplotlib and Seaborn are libraries used for data visualization in Python.

# 1. Matplotlib
# Matplotlib is a basic plotting library used to create graphs and charts such as line charts, bar charts, histograms, and scatter plots.

# Example
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 2. Seaborn
# Seaborn is built on top of Matplotlib and is used for advanced statistical visualizations with better design and appearance.
# Example
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 40, 50]

sns.histplot(data)

plt.show()

# Example Dataset
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Kiran", "Meena"],
    "Marks": [85, 78, 90, 88],
    "StudyHours": [5, 4, 6, 5]
}

df = pd.DataFrame(data)
#1. Bar Chart (Marks Comparison)
import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# 2. Line Chart (Trend Analysis)
plt.plot(df["Name"], df["Marks"])
plt.title("Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot (Relationship Between Variables)
plt.scatter(df["StudyHours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()

# 4. Histogram using Seaborn
import seaborn as sns

sns.histplot(df["Marks"])
plt.title("Marks Distribution")

plt.show()

# Example: Simple Dashboard for Dataset Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "StudyHours": [2, 3, 4, 5, 6, 7],
    "Marks": [50, 55, 65, 70, 80, 90],
    "SleepHours": [7, 6, 7, 8, 6, 7]
}

df = pd.DataFrame(data)

# Create dashboard layout
plt.figure(figsize=(10,6))

# Scatter plot: Study Hours vs Marks
plt.subplot(2,2,1)
sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.title("Study Hours vs Marks")

# Line chart
plt.subplot(2,2,2)
plt.plot(df["StudyHours"], df["Marks"])
plt.title("Marks Trend")

# Histogram
plt.subplot(2,2,3)
sns.histplot(df["Marks"])
plt.title("Marks Distribution")

# Heatmap (relationship between features)
plt.subplot(2,2,4)
sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation")

plt.tight_layout()
plt.show()
