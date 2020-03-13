# Data Types
word = "I am a string"

# Can be operated with +, -, *, /, %
number = 5      # Integer
number_2 = 7.5  # Float

# Boolean, Ture or False
switch = True

# Baisic Operators
Test1 = 6
Test2 = 2.5
Test3 = 3

# Addition / Subtraction
Addition = Test1 + Test2
Subtraction = Test1 - Test2

# Multiplication / Division 
Multiplication = Test1 * Test2     # float * int gives float
Multiplication2 = Test1 * Test3    # int * int gives int
Division = Test1 / Test3           # all division returnes a float
Division2 = Test1 // Test3         # // keeps the value as int

# Modulo
Modulo = 5 % 2  # returnes the remainder

# Convert Datatypes
convert = int(4.9)                 # Converts to int, drops the decimal from a float. 
convert2 = int(Addition)           # The output always rounds down
convert3 = float(6.1234)           # Converts to float
convert4 = str(convert3)           # Converts to string

# Concatemation - combining of strings
string1 = "Goodbye"
String2 = "Us Dollar"

combine = string1 + " " + String2

print(combine)