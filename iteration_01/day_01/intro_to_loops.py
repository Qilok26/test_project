"""
Lesson: Data Types, Variables, and Why Loops Are Necessary
----------------------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice patterns.
"""

# --- Section 1: Variables and Data Types ---

# TODO: Create a variable called name that stores your name
name = "Kevin"
# TODO: Create a variable called age that stores your age
age = 30
# TODO: Create a variable called pi that stores the value 3.14159
pi = 3.14159

# Print each variable

print("Name:",name)
print("Name: " + name)
print(f"Name: {name}") # F Strings are really nice for formatting purposes

print("Age:",age)
print("Age: " + str(age))
print(f"Age: {age}")

print("Pi:",pi)
print("Pi: " + str(pi))
print(f"Pi: {pi}")

print(f"Hello there my name is {name} and I am {age} years old. Here are some digits of pi: {pi}")


# --- Section 2: Why Loops? ---

# Imagine you want to print the numbers 1 through 10.
# First, try it the "long way".

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# TODO: Keep going until you reach 10

# Question for you:
#   What happens if I want to print 1 through 100? Or 1 through 1000?
#   Is it realistic to keep writing print statements forever?

# ANSWER: No. Really tedious. Inefficient use of code. Code is less readable.


# --- Section 3: For Loops ---
# TODO: Replace the repeated print statements above with a for loop.

# Example starter (fill in the blanks):
for i in range(1,101):
    print(i)

# Hint: What does range(start, stop) do?

# ANSWER: It returns you a list of values ranging from the start value up until the stop value (not including the stop value)


# --- Section 4: While Loops ---
# A while loop repeats until a CONDITION is no longer true.

# TODO: Try to print numbers 1 through 10 using a while loop.

# Example starter:
    # TODO: Don’t forget to change x, or your loop will run forever!
x = 1
while x<= 10:
    print(x)
    x = x + 1 # x += 1 is a way for you to shorten this logic a bit


# --- Section 5: Reflection ---
# Answer these questions (in comments):
# 1. Why is a loop better than writing 100 print statements?

# ANSWER: Makes code much more efficient. Makes code more readable and reduces line count.

# 2. What does a loop REQUIRE in order to work?
#    (Think: starting point, stopping condition, something that changes)

# ANSWER: A for loop requires either some list to iterate through until the list is complete or you break out of the loop.
#         A while loop requires some starting boolean value (True or False) that will allow the loop to begin. Once the 
#         value changes, the loop will end.

