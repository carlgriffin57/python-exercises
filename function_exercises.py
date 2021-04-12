# Define a function named is_two. It should accept one input and return True if the passed input is either the 
# number or the string 2, False otherwise.
def is_two(num):
    # Check to see if num is the number 2 or the string 2
    if num == 2 or num == '2':
        # return True if that is the case
        return True
    else:
        # return False if that is not the case
        return False

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    # Check to see if the letter is one of the vowels a,e,i,o,u
    if letter in 'aeiou':
        # return True if it is a vowel
        return True
    else:
        # return False if it is not a vowel
        return False

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(letter):
    # Check to see if the letter is not one of the vowels a,e,i,o,u
    if letter not in 'aeiou':
        # return True is it is not a vowel
        return True
    else:
        # return False if it is a vowel
        return False

# Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.
def is_word(word):
    # Check to see if the first letter of the word is not a vowel a,e,i,o,u
    if word[0].lower() not in 'aeiou':
        # If is not a vowel then return the word capitalized
        return word.capitalize()
        # Otherwise the word begins with a vowel so just return the word
    return word

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and 
# the bill total, and return the amount to tip.
def calculate_tip(tip_rate, bill_total):
    # Take the tip_rate and bill_total and calculate the tip amount
    tip = tip_rate * bill_total # tip rate should be between 0 and 1
    # return the tip amount rounded to 2 decimals
    return round(tip, 2)

# Define a function named apply_discount. It should accept a original price, and a discount percentage, and 
# return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    new_price = original_price - (original_price * (discount_percentage / 100))
    return(round(new_price, 2))

# Define a function named handle_commas. It should accept a string that is a number that contains commas in 
# it as input, and return a number as output.
def handle_commas(number):
    # Return the number after stripping out all the commas
    return number.replace(',','')

# Define a function named get_letter_grade. It should accept a number and return the letter grade associated 
# with that number (A-F).
def get_letter_grade(number):
    # if the number grade is higher or equal to 90 then return the letter 'A'
    if number >= 90:
        return('A')
    # if the number grade is higher or equal to 80 then return the letter 'B'
    elif number >= 80:
        return('B')
    # if the number grade is higher or equal to 70 then return the letter 'C'
    elif number >= 70:
        return('C')
    # if the number grade is higher or equal to 60 then return the letter 'D'
    elif number >= 60:
        return('D')
    # if the number grade is less than 60 then return the letter 'F'
    else:
        return('F')

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    # Assign the vowels a,e,i,o,u to a variable called vowels
    vowels = ('a', 'e', 'i', 'o', 'u') 
    # loop through the string letter by letter and strip out the vowels plus lower case the string
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
    return string

# Define a function named normalize_name. It should accept a string and return a valid python identifier, 
# that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
import re

def normalize_name(s):

    # Replace blank spaces with underscores and remove invalid characters
    s = s.replace(' ','_')
    s = re.sub('[^0-9a-zA-Z_]', '', s)
   
    # Remove leading characters until we find a letter then lowercase everything
    s = re.sub('^[^a-zA-Z]+', '', s)
    s = s.lower()
    return s
# Send the function a string of characters to test the code
s = normalize_name(' % First Name')
print(s)

# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative 
# sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(numbers):
    # return the cumulative sum of a list of numbers
    return [sum(numbers[:i]) for i in range(1, len(numbers)+1)]
