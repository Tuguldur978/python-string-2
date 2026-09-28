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
print(is_valid_email("hello@gmail.com"))

# Exercise 2
def remove_vowels(text):
     a = ""
    for char in text:
        if char not in "aeiouAEIOU":
            a += char
    return a
print(remove_vowels("Please call me tomorrow"))
 
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

