# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    at = False
    dot = False
    for char in text:
        if char == "@":
            at = True
        elif char == ".":
            dot = True
    if at and dot:
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
        words = text.split()
        for word in words:
            remove_word = ""
            for char in word:
                if char.isdigit():
                    remove_word += char
            if len(remove_word) == 4:
                return remove_word
        return False

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

