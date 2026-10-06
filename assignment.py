# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    r = 0
    c = 0
    for char in text:
        if char == "@":
            r += 1
        if char == ".":
            c += 1
    if r >= 1  and c >= 1:
        return "Valid"
    else:
        return "Invalid"

# Exercise 2
def remove_vowels(text):
    result = ""
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            result += ""
        else:
            result += char
    return result
 
# Exercise 3
def get_initials(text):
    # Write your code here
    pass

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

