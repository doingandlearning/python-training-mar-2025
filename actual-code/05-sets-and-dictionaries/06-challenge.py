# List Comprehension Exercise: Filtering and Transforming Data
# Task:
# Given a list of words, write a list comprehension that:
#
# Filters out words shorter than 4 characters.
# Converts the remaining words to uppercase.
# Appends the length of each word to a tuple.
# Example Input:
# words = ["apple", "bat", "carrot", "dog", "elephant"]
# Expected Output:
# [('APPLE', 5), ('CARROT', 6), ('ELEPHANT', 8)]
# Your Task:
# Write a one-liner using list comprehension to achieve this.

words = ["apple", "bat", "carrot", "dog", "elephant"]

filtered_words = [(value.upper(), len(value)) for value in words if len(value) > 3]

print(filtered_words)