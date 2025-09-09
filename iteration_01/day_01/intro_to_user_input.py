"""
Lesson: Loops, Conditionals, and User Input
-------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how programs can respond to user input.
"""

# --- Section 1: Getting Input from the User ---

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name: ")

# TODO: Ask the user for their age and store it as an integer
age = int(input("What is your age: "))

# Print out a greeting
print(f"Hello, {name}")
print(f"You are {age} years old")


# --- Section 2: Conditionals with Input ---

# TODO: Check if the user is old enough to vote (18+)
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# TODO: Ask the user for a number and check if it's even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# --- Section 3: Loops with Input ---

# Problem: You want to ask a user for 5 test scores and print them
# without loops, you'd have to write 5 separate inputs.  

# TODO: Try writing 5 input statements manually first (commented out)
score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
print(score1)
print(score2)
# ...

# Question: How could a loop make this easier?

# ANSWER: Since I know I want to run this 5 times, I can use a for loop to reduce the number of lines
#         needed to solve this problem.


# --- Section 4: For Loops with Input ---

# TODO: Use a for loop to ask for 5 test scores and print each one
# Example starter:
for i in range(5):
    score = int(input(f"Enter Score {str(i + 1)}: "))
    print(f"You entered: {score}")


# --- Section 5: While Loops with Input ---

# TODO: Keep asking the user to enter a positive number
# until they actually do. Use a while loop.
# Example starter:
num = int(input("Enter a positive number: "))
while num < 0:
    print("That is not positive. Try again!")
    num = int(input("Enter a positive number: "))
print(f"Thank you! You entered: {num}")


# --- Section 6: Challenges ---

# 1. Ask the user for a number and tell them if it's divisible by 3, 5, or both
# 2. Ask the user for their favorite color repeatedly until they type "stop"
# 3. Create a mini grading program:
#     - Ask the user for scores until they type -1
#     - Keep track of how many scores are passing (>= 60)
#     - Print a summary at the end

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"The number {num} is divisible by both 5 and 3")
elif (num % 3 == 0):
    print(f"The number {num} is divisible by 3")
elif (num % 5 == 0):
    print(f"The number {num} is divisible by 5")
else:
    print(f"The number {num} is not divisible by either 5 or 3")


# --- Section 7: Reflection ---
# 1. How does using input change the way your program works compared to fixed variables?

# ANSWER: Interacting with the user through text allows the user to have more control over the program. 
#         This allows the program to be a bit more dynamic and tailored to the user experience.

# 2. How do loops and conditionals work together when handling user input?

# ANSWER: Loops and conditionals work together when handling user input primarily to ensure input validation
#         and to control program flow based on user choices.

# 3. What are some real-world programs where loops + conditionals + input are all necessary?

# ANSWER: During a workout, I want to continue doing sets of a certain exercise until my muscles are too tired.
#         So once muscles_too_tired == True I will not engage in another workout set.