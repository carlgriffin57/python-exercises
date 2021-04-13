# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# import the module and refer to the function with the . syntax
import function_exercises
function_exercises.remove_vowels('hello')

# use from to import the function directly
from function_exercises import handle_commas
print(handle_commas('1,234,567'))

# use from and give the function a different name
from function_exercises import calculate_tip as ct
print(ct(.20,40))

# For this exercise, read about and use the itertools module from the standard library to help you solve the 
# problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product
print(f"There are {len(list(product('abc', '123')))} different ways.")

# How many different ways can you combine two of the letters from "abcd"?
from itertools import permutations
print(f"There are {len(list(permutations('ABCD', 2)))} permutations.")

# Save this file as profiles.json inside of your exercises directory. Use the load function from the json 
# module to open this file, it will produce a list of dictionaries. Using this data, write some code that 
# calculates and outputs the following information:
import json
with open('/Users/carlg/codeup_data_science/python_exercises/profiles.json') as profiles:
    profiles_dict = json.load(profiles)

# Total number of users
print(len(profiles_dict))

# Number of active users
counter = 0
for profile in profiles_dict:
    if profile['isActive'] == True:
        counter += 1
print(f"There are {counter} active users.")

# Number of inactive users
counter = 0
for profile in profiles_dict:
    if profile['isActive'] == False:
        counter += 1
print(f"There are {counter} inactive users.")

# Grand total of balances for all users
balances = []
new_balances = []
for profile in profiles_dict:
    balances.append(profile['balance'])
for balance in balances:                 
    balance = balance.replace("$", '')    
    balance = balance.replace(",","")
    new_balances.append(float(balance))
print(f"The total balance of all the users is: {sum(new_balances)}")

# Average balance per user
balances = []
new_balances = []
for profile in profiles_dict:
    balances.append(profile['balance'])
for balance in balances:                 
    balance = balance.replace("$", '')    
    balance = balance.replace(",","")
    new_balances.append(float(balance))
print(f"The average balance of per user is: {round(sum(new_balances) / len(new_balances), 2)}")

# User with the lowest balance
balances = []
new_balances = []
for profile in profiles_dict:
    balances.append(profile['balance'])
for balance in balances:                 
    balance = balance.replace("$", '')    
    balance = balance.replace(",","")
    new_balances.append(float(balance))
print(f"The user with the smallest balance is: {profiles_dict[new_balances.index(min(new_balances))]['name']}")

# User with the highest balance
balances = []
new_balances = []
for profile in profiles_dict:
    balances.append(profile['balance'])
for balance in balances:                 
    balance = balance.replace("$", '')    
    balance = balance.replace(",","")
    new_balances.append(float(balance))
print(f"The user with the highest balance is: {profiles_dict[new_balances.index(max(new_balances))]['name']}")

# Most common favorite fruit
from collections import Counter

favorite_fruits = []
for profile in profiles_dict:
    favorite_fruits.append(profile['favoriteFruit'])

print(f"The most favorite fruit is: {(Counter(favorite_fruits).most_common()[0])}")

# Least most common favorite fruit
from collections import Counter

favorite_fruits = []
for profile in profiles_dict:
    favorite_fruits.append(profile['favoriteFruit'])

print(f"The least favorite fruit is: {(Counter(favorite_fruits).most_common()[-1])}")
# Total number of unread messages for all users
import re

list_of_greetings = []
# number_strings_of_unread_emails = []
list_of_numbers = []
for profile in profiles_dict:
    list_of_greetings.append(profile['greeting'])
for item in list_of_greetings:
    s = [int(item) for item in re.findall(r'-?\d+\.?\d*', item)]
    list_of_numbers.append(s)
print(f"The sum of all unread emails is: {sum([int(item[0]) for item in list_of_numbers])}")