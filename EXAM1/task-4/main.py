# Function: FizzBuzz
# Objective: Create a function `fizz_buzz` that evaluates the divisibility of a number by 3 and 5.
# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the number as a string.
# Parameters:
# - num: An integer to be evaluated.
# Returns:
# - A string based on the criteria above.

num = 9
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(str(num))

num = 25
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(str(num))

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(str(num))

num = 4
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(str(num))