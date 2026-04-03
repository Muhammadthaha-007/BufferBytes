# def reverse_string(s):
#     rev = ""
#     for ch in s:
#         rev = ch + rev
#     return rev
# print(reverse_string("Python"))

# def palidrome(s):
#     s = s.lower()
#     rev = ""
#     for ch in s:
#         rev = ch + rev

#     return s == rev
# print(palidrome("Madam"))

# def sec_largest(num_list):
#     largest = max(num_list)
#     num_list.remove(largest)
#     second = max(num_list)

#     return second
# print(sec_largest([10, 20, 4, 45, 99]))

# def find_minimum(num_list):
#     minimum = float('inf')
#     for num in num_list:
#         if num < minimum:
#             minimum = num
#     return minimum
# print(find_minimum([3, 1, 7, 2, 9]))

# def vovels_count(s1):
#     vovels = "aeiou"
#     count = 0

#     for ch in s1.lower():
#         if ch in vovels:
#             count += 1
#     return count

# print(vovels_count("programming"))


# def factorial(n):
#     if n < 0:
#         return None
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# def sum_dig(n):
#     s = 0
#     while n > 0:
#         s += n % 10
#         n = n // 10
#     return s
# print(sum_dig(1234))


# def missing_number(n):
#     actual_sum = sum(n)
#     largest = max(n)
#     expected_sum = largest * (largest + 1) // 2

#     return expected_sum - actual_sum

# print(missing_number([1, 2, 4, 5]))


# def end_is_zero(nums):
#     count_zero = 0
#     for num in nums:
#         if num == 0:
#             nums.remove(num)
#             count_zero += 1
#     for zero in range(count_zero):
#         nums.append(0)

#     return nums

# print(end_is_zero([0, 1, 0, 3, 12]))
    

# def longest_word(s):
#     words = s.split()
#     longest = ""

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     return longest

# print(longest_word("I love programming in python"))

# def count_word(s):
#     count = 1
#     for space in s:
#         if space == " ":
#             count += 1
#     return count
# print(count_word("I love python"))

# def filter_data(*args, **kwargs):
#     print("Numbers > 10:")
#     for num in args:
#         if type(num) == int and num > 10:
#             print(num)
#     print("\nString Details:")
#     for key,val in kwargs.items():
#         if type(val) == str:
#             print(f"{key} : {val}")

# filter_data(5, 12, 3, 20,"hello", name="Thaha", age=25, city="Calicut")

# def remove_dup(nums):
#     seen = set()

#     for num in nums:
#         if num not in seen:
#             seen.add(num)
#         else:
#             continue
#     return list(seen)
# print(remove_dup([1, 2, 2, 3, 1, 4]))

# def non_repeating(s):
#     count = {}
#     for ch in s:
#         count[ch] = count.get(ch,0) + 1
#     for ch in s:
#         if count[ch] == 1:
#             return ch
#     return None

# print(non_repeating("aabbcde"))

# Excel_table = [
#     {
#       "Name": "Abuharis",
#     "age": 18,
#     "Full Name": "Abuharis Salih",
#     "Qualitication": "Degree",
#     "Gender": None,
#     "Vaccine": True 
#     },
#     {
#     "Name": "User2",
#     "age": 18,
#     "Full Name": "Abuharis User2",
#     "Qualitication": "Degree",
#     "Living_Status": "Abroad"
#     },
#     {
#          "Name": "User3",
#     "age": 18,
#     "Full Name": "Abuharis User2",
#     "Qualitication": ["Degree", 10, 12],
#     "Gender": True,
#     "Vaccine": True,
#     }
#     ]

# def finder(data):
#     for dic in data:
#         for key, val in dic.items():
#             if type(val) == list:
#                 for v in val:
#                     if v == 12:
#                         return dic["Name"]
#     return None

# print(finder(Excel_table))

# def add_up_to_target(nums,target):
#     seen = {}
#     for num in nums:
#         com = target - num
#         if com in seen:
#             return [num, com]
#         seen[num] = True
#     return None

# print(add_up_to_target([3, 2, 4],6))

# def move_zero(nums):
#     zero_count = 0

#     for num in nums:
#         if num == 0:
#             zero_count += 1
#             nums.remove(num)
#     for zero in range(zero_count):
#         nums.append(0)
#     return nums

# print(move_zero([0, 1, 0, 3, 12]))


# def sec_largest(nums):
#     num = set(nums)
#     largest = max(num)
#     num.remove(largest)
#     sec = max(num)
#     return sec

# print(sec_largest([10, 20, 20, 5]))


# n = 12345
# temp = n
# digits = []
# rows = 5

# while temp > 0:
#     digits.insert(0,temp % 10)
#     temp //= 10

# for row in range(rows):
#     for col in range(rows):
#         if row == 0:
#             print(digits[col], end="")

#         elif row == 1:
#             if col == 0 or col == rows - 1:
#                 print(digits[col], end="")
#             else:
#                 print(" ", end="")

#         else:
#             if col == row or col == rows - row - 1:
#                 print(digits[col], end="")
#             else:
#                 print(" ", end="")
#     print()


# rows = 4

# for row in range(1,rows+1):
#     for col in range(row,0,-1):
#         print(col,end="")
#     print()

# rows = 5

# for row in range(rows):
#     for col in range(rows-1):
#         if row in [x for x in range(rows)] and col in [rows - rows, rows - 2] or \
#              row == 2 and col in (x for x in range(rows - 1)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()+


# rows = 6

# for row in range(rows):
#     for col in range(row):
#         print(row, end="")
#     print()


rows = 6

for upper in range(rows):
    for col in range(upper):
        print("*",end="")
    print()
for lower in range(rows,0,-1):
    for col in range(lower):
        print("*",end="")
    print()