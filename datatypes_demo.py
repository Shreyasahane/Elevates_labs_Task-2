# Declare a variables in different datatypes
# int
a = 10
b = 6.7
c = 'Shreya'
d = True

# print the datatype of each variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Perform arithmetic operations 
num1 = 20
num2 = 2
add =num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
floor = num1 // num2
power = num1 ** num2

# print the result of all arithmetic opeartions
print("Addition: ",add) # print addition
print("Substraction: ",sub) # print Substraction
print("Multiplcation: ",mul) #print Multiplication
print("Division: ",div) # Print Division
print("Modulus: ",mod) # Print remainder
print("Floor Division: ", floor) # print the integer quotient
print("Power: ",power) # print power of a number

# 4. Take string input and convert using type casting
user_input =input("Enter a number: ")

try:
    # convert string into integer
    num1 = int(user_input)     # Conversion from string to int
    print("Converted to int:", num1)

    # convert string to float
    num2 = float(user_input) # conversion string to float
    print("Converted to float: ",num2)

except ValueError:
    # Handles invalid inputs like symbols or letters
    print("Please enter a valid number")

# Concatenate strings and numbers properly
age = 20
name = "Shreya"

message = "My name is " + name + " and i am " + str(age) + " year's old ."
print(message)

# Demonstrate dynamic typing by reassigning variable values.
var = 100 # var is int
print("var = ", var ,"Type: ",type(var))

var = 10.0 # now var is float
print("var = ", var ,"Type: ",type(var))

var = 'Shreya' # now var is string
print("var = ", var ,"Type: ",type(var))

var = True # now var is boolean
print("var = ", var ,"Type: ",type(var))
