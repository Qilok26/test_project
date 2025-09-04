"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["pizza", "ice cream", "cheescake", "pretzels", "porrage"]

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?

#foods[100]

# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append("brocolli")

# TODO: Insert a food at the beginning with .insert()

foods.insert(0, "banana")

# TODO: Remove one food from the list with .remove()

foods.remove("pizza")

# TODO: How many foods are in the list? Use len()

#6
print(len(foods))

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?
#Cause it cant find chocolate

#foods.remove("chocolate")
# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.

for item in foods:
    print(item)
# Bug Exploration:
# Change your loop to go past the length of the list:
#for i in range(50):
#    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?
#Cause it goes outside of the arranged length

# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me2 = {
    "name": "Kevin",
    "age": 30,
    "student": False
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.

me = {
    "name": "Georgii",
    "age": 17,
    "student": True,
    "color": "blue"
    }

# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")
print(me['name'])
print(me['age'])
print(me['color'])



# Bug Exploration:
# Try printing a key that doesn’t exist.
#print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?
#It's a KeyError — you can check if the key is there with "key" in dict or use .get() so it doesn't break.

# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.

me["hometown"] = "Russia"

# TODO: Change the value of an existing key.

me["age"] = 18

# TODO: Remove one key-value pair.

me.pop("name")

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?

# This causes a KeyError because "grade" isn't in the dictionary.
# It's similar to removing an item from a list that doesn't exist — it crashes.

# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()
for key, value in me.items():
    print(f"{key}: {value}")

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?
# A: Because looping over a dictionary by default only gives the keys.

# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
friends = [
    {"name": "Sam", "food": "pizza"},
    {"name": "Jamie", "food": "sushi"},
    {"name": "Taylor", "food": "tacos"}
]

# TODO: Print the favorite food of the second friend.
print(friends[1]["food"])

# TODO: Loop through and print "<name> likes <food>" for each friend.

for friend in friends:
    print(f"{friend['name']} likes {friend['food']}")

# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?
# print(friend["hobby"])  # This will cause a KeyError
# A: Use `.get("hobby")` instead, which returns None (or a default) instead of crashing.

# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# A: A list stores items in order using numbers (indexes), a dictionary uses keys and values.
# 2. When would you want to use a dictionary instead of a list?
# A: When you want to label your data with keys and look things up quickly.
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# A: Yes — like storing a list of students, where each student has a name, grade, and email.
# 4. What types of mistakes gave you the most errors today?
# A: Trying to access keys that don’t exist and forgetting to use `.items()` in loops.
# 5. How might noticing errors actually help you learn?
# A: Errors show what went wrong, so you can fix your thinking and remember it better next timejkopi