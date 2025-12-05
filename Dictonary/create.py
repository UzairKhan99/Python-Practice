# ============================
# CREATING FUNCTIONS IN PYTHON
# ============================
#
# A function is a block of code that runs only when you "call" it.
# It helps you avoid repeating the same code again and again.
#
# Basic syntax:
#   def function_name():
#       # code block (indented)
#
# Then call it using:
#   function_name()

print("=== 1) Basic function with no parameters ===")

# Function definition


def greet():
    # This code runs when we call greet()
    print("hi there")


# Function call
greet()   # output: hi there


print("\n=== 2) Function with a parameter (input) ===")

# Here, "name" is a parameter (like a variable)


def greet_person(name):
    print("Hello,", name)


# Call the function with an argument (actual value)
greet_person("Uzair")
greet_person("Ali")


print("\n=== 3) Function with two parameters and return value ===")

# This function adds two numbers and RETURNS the result


def add(a, b):
    result = a + b
    return result   # send the value back to the caller


# Use the function and store the result
sum_result = add(10, 20)
print("add(10, 20) =", sum_result)

# You can also print directly
print("add(5, 7) =", add(5, 7))


print("\n=== 4) Function with default parameter ===")

# "country" has a default value "Pakistan"


def greet_country(name, country="Pakistan"):
    print(f"{name} is from {country}")


greet_country("Uzair")               # uses default country
greet_country("John", "USA")         # overrides default


print("\n=== 5) Why use functions? ===")
print("- Reuse code easily")
print("- Make code cleaner and easier to read")
print("- Avoid copy-pasting the same logic many times")

# Quick summary (as comments):
# def func_name():
#     # code
#
# def func_name(param1, param2):
#     # code
#     return value
#
# Call with: func_name(args...)
