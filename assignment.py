# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    has_at = False
    has_dot = False

    for char in text:
        if char == "@":
            has_at = True
        elif char == ".":
            has_dot = True

    if has_at and has_dot:
        return "Valid"
    else:
        return "Invalid"


# Exercise 2
def remove_vowels(text):
        vowels = "aeiouAEIOU"
        result = ""
        for char in text:
            if char not in vowels:
                result += char
        return result
 
# Exercise 3
def get_initials(text):
        words = text.split()
        initial = ""
        for word in words:
            initial += word[0].upper() + "."
        return initial
        

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

