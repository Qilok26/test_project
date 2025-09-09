"""
Lesson: Conditionals in Python
------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how conditionals change what happens.
"""

# --- Section 1: True or False? (Boolean Expressions) ---

# Conditionals always depend on something being True or False.
# Let's explore.

# TODO: Create two variables. One that represents age, and the other a boolean that is True if you are a student and false if you are not:
age = 30
is_student = False

# What happens when we compare numbers?
print("Is age greater than 18?", age > 18)
print("Is age less than 13?", age < 13)

# What happens when we compare equality?
print("Is age exactly 16?", age == 16)

# What happens when we use a variable directly?
print("Is student status True?", is_student)

# Reflection Question (write your answer in a comment):
# Q: Why do all of these print either True or False?

# ANSWER: Boolean's are defined by a logical statement between somethings status as being True or False

# --- Section 2: If Statements ---

# Problem: You want to check if someone can vote (age >= 18).
# First, try without conditionals (just print something no matter what).

print("You can vote!")   # TODO: What’s wrong with this approach?

# ANSWER: It will always print that you can vote. Not based on age variable value.


# Now add an IF statement:

if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote")

# --- Section 3: If/Else ---

# Else statement also above

# TODO: Write a program that checks if a number is even or odd.
# Steps to guide you:
# 1. Make a variable called num
num = 21
# 2. Use the modulo operator (%) to check if num % 2 == 0
if num % 2 == 0:
# 3. If even, print "Even number"
    print("Even number")
# 4. Otherwise, print "Odd number"
else:
    print("Odd number")

# --- Section 4: If / Elif / Else ---

# TODO: Imagine a grading system:
#   - 90 or above → "A"
#   - 80 or above → "B"
#   - 70 or above → "C"
#   - 60 or above → "D"
#   - below 60   → "F"


# Write this using if, elif, and else statements.
grade = 82

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# --- Section 5: Nesting Conditionals ---

# TODO: Ask two questions:
#   1. Is the person a student?
#   2. Is their age under 18?
# If both are true, print "You are a student and a minor."
# Otherwise, print something else.

is_student = False
age = 17

if is_student == True and age < 18:
    print("You are a student and a minor")
else:
    print("You are either not a student, not a minor, or both...")
    


# --- Section 6: Reflection ---
# Answer in comments:
# 1. What does a conditional REQUIRE in order to run effectively?
    # ANSWER: it requires some logical statement that results in either a truth or a false status. Either with a boolean
    # statement or a boolean variable.
# 2. How do elif and else make your code shorter or more readable?
    # Improves code readability with conditional logic. It is more efficient than using multiple independent if statements
    # or deeply nested if-else blocks.
# 3. Can you think of a situation in real life where you’d use multiple conditionals?
    # If I am sick and if it is a week day then I need to call out of work. Otherwise, I won't need to call out of work at all.
    # Since I will either not be sick, it will not be a weekday, or both simultenously, the else statement catches all those cases.