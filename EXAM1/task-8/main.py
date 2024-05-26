# Function: Pair Characters
# Objective: Write a function `pair_characters` that takes a string and returns a list of two-character pairs.
# If the string has an odd number of characters, append an asterisk '*' to the final pair to ensure all pairs consist of two characters.
# Parameters:
# - s: A string to be processed into pairs.
# Returns:
# - A list of two-character pairs.

def pair_characters(s):
    for i in range(0, len(s), 2):
        yield s[i:i+2]
    if len(s) % 2 != 0:
        yield s[-1] + "*"

# Example usage:
print(list(pair_characters("Hello")))
print(list(pair_characters("Characters")))
print(list(pair_characters("ABCDEF")))
print(list(pair_characters("a")))
# Example usages:
# print(pair_characters("hello"))  # Output: ['he', 'll', 'o*']
# print(pair_characters("characters"))  # Output: ['ch', 'ar', 'ac', 'te', 'rs', '*']
# print(pair_characters("abcdef"))  # Output: ['ab', 'cd', 'ef']
# print(pair_characters("a"))  # Output: ['a*']
