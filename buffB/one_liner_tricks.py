# Python one-liner Tricks cheatsheet

# 1. Reverse a string

# rev = "Python" [::-1]
# print(rev)

# 2. Check if Palidrome

# is_palindrome = lambda word: word.lower() == word.lower()[::-1]
# print(is_palindrome("Madam"))

# square 

# square = lambda x: x * x
# print(square(5))

# Maximum

# maximum = lambda a, b: a if a > b else b
# print(maximum(10,25))

# check = lambda s: "Even Length" if len(s) % 2 == 0 else "Odd Length"

# print(check("madam"))

# num_list = [10, 5, 3, 4, 3, 5, 6]
# count = {}

# for i in num_list:
#     count[i] = count.get(i,0) + 1

# for k,v in count.items():
#     if v != 1:
#         print(k)
#         break

