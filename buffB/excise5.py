# amstrong = []
# not_amstrong = []

# for i in range(1,501):
#   n =  0
#   x = i
#   while x > 0:
#     digits = x % 10
#     qube = digits ** 3
#     n = n + qube
#     x = x // 10
#   if n == i:
#     amstrong += [i]
#   else:
#     not_amstrong += [i]
# for i in amstrong:
#   print(f"amstrong = {i}")
# for i in not_amstrong:
#   print(f"Not_amstrong = {i}")

# def is_palindrome(num):
#   rev = 0
#   org = num
#   while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10

#   if rev == org:
#     return True
#   return False
# print(is_palindrome(121))


# def find_duplicates(nums):
#   seen = set()
#   dup = set()
#   for num in nums:
#     if num in seen:
#       dup.add(num)
#     else:
#       seen.add(num)
#   return list(dup)
# print(find_duplicates([1,2,3,4,2,5,6,3,1]))



# n = int(input("Enter the number :"))
# def is_amstrong(n):
#     og = n
#     dig = len(str(og))
#     am = 0

#     while n > 0:
#         rem = n % 10
#         am = am + rem ** dig
#         n //= 10

#     return og == am
# print(f"Amstrong:{is_amstrong(n)}")


# num_list = [1, 2, 3, 4, 2, 5, 3]

# unique = []

# for num in num_list:
#     if num in unique:
#         print(num)
#         break
#     else:
#         unique.append(num)

# def first_dup(nums):
#     seen = {}

#     for num in nums:
#         if num in seen:
#             return num
#         seen[num] = 1

#     return None

# print(first_dup([1, 2, 3, 4, 2, 5, 3]))

# def anagram(str_input1,str_input2):
#     if len(str_input1) != len(str_input2):
#         return False

#     count1 = {}
#     count2 = {}

#     for str_input in str_input1:
#         count1[str_input] = count1.get(str_input,0) + 1
#     for str_input in str_input2:
#         count2[str_input] = count2.get(str_input,0) + 1

#     return count1 == count2

# print(anagram("hello", "world"))

