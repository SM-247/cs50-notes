# Take input from the user
input_string = input("Enter a string: ")

# Using a list comprehension to filter out only alphanumeric characters
result = [char for char in input_string if char.isalnum()]
import re

# Take a input_string as input from the user

# Split the input_string into sentences using '.', '!', and '?' as delimiters
sentences = re.split(r'[.!?]', input_string)

# Remove any empty strings or extra spaces from the result
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
words=input_string.split()
print(sentences)
print(words)
print(result)
