# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
        at = False
        dot = False
        for char in text:
            if char == "@":
                has_at = True
            elif char == ".":
                has_dot = True
    if  at and dot:
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
    words = name.split()
    a = ""
    for word in words:
        a += word[0].upper() + "."
    return a

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

