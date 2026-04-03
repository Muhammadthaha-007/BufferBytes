# data_range = int(input("Enter the range :"))
# data = []
# if data_range < 2:
#     print("OOPS!..At least 2 length needed!")
# else:
#     for i in range(data_range):
#         num = int(input(f"Enter the item no {i+1}:"))
#         data.append(num)
#     sorted_set = sorted(set(data))
#     if len(sorted_set) == 1:
#         print(f"all are same!, data = {sorted_set[0]}")
#     else:
#         print(f"Largest no : {sorted_set[-1]}")
#         print(f"Second Largest : {sorted_set[-2]}")


# row = 10
# for i in range(row):
#     for j in range(i+1):
#         if i == j or j == 0 or i == row - 1:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# list_of_words = ["pen", "book", "pen", "laptop", "book", "pen"]
# count = {}
# for i in list_of_words:
#     count[i] = count.get(i,0) + 1
# print(count)

# def factorial(n):
#     fact = 1
#     while n > 1:
#         fact = fact * n
#         n -= 1
#     return fact

# print(factorial(5))

# def factorial(n):
#     fact = 1
#     for i in range(n,1,-1):
#         fact = fact * i
#     return fact
# print(factorial(5))

# list_num = [1, 2, 2, 3, 1, 4]
# uniq = []
# for i in list_num:
#     if i not in uniq:
#         uniq.append(i)
# print(uniq)

# items = ["pen", "book", "pen","pen", "laptop"]
# unique = list(dict.fromkeys(items))
# print(unique)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name :",self.name)
#         print("Age :",self.age)
# obj = Person("Rahul",25)
# obj.display()


# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#     def subtract(self):
#         return self.a - self.b
#     def multiply(self):
#         return self.a * self.b 

# obj = calculator(10,50)
# print("addition : ",obj.add())
# print("Substract : ",obj.subtract())
# print("Multiply:",obj.multiply())


# a = 10
# b = 20
# a,b = b,a
# print("a = ",a,"\nb = ",b)

# n = 3
# is_prime = True
# for i in range(2,int(n ** .5)+1):
#     if n % i == 0:
#         is_prime = False

# if is_prime:
#     print("Prime")
# else:
#     print("NOT")

# print(int(n ** .5))

# def is_amstrong(n):
#     org_num = n
#     temp = n
#     digits = 0

#     while n > 0:
#         digits += 1
#         n //= 10
#     amstrong = 0
#     while temp > 0:
#         rem = temp % 10
#         amstrong = amstrong + rem ** digits
#         temp //= 10

#     return amstrong == org_num

# print("Amstrong:",is_amstrong(1634))

# n = int(input("Enter a Number : "))
# rev = 0

# while n > 0:
#     reminder = n % 10
#     rev = rev * 10 + reminder
#     n //= 10
# print(rev)

# list_num = [1, 2, 3, 4,5]
# sum_list = 0

# for i in list_num:
#     sum_list += i
# print(sum_list)

# dict_data = {'a': 10, 'b': 25, 'c': 15}
# largest = dict_data['a']

# for item in dict_data.items():
#     if item[1] > largest:
#         largest = item[1]
# for k,v in dict_data.items():
#     if v == largest:
#         print("Key with max value:",k)

# Fibonacci series
# n = int(input("Enter the range : "))

# a = 0
# b = 1

# for i in range(n):
#     print(a,end=" ")
#     a, b = b, b+a

# nums = [1, 2, 5, 7]
# for i in range(len(nums)-1):
#     current = nums[i]
#     next_num = nums[i+1]
#     if next_num - current > 1:
#         for missing in range(current + 1,next_num):
#             print("Missing number :",missing)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5]

# intersection_list = []

# for i in list1:
#     if i in list2:
#         intersection_list.append(i)

# print(intersection_list)

# list_num = [6,1, 2, 3, 4, 5]

# for i in range(len(list_num)-1):
#     ind0 = list_num[i]
#     ind1 = list_num[i+1]
#     if ind1 < ind0:
#         is_sorted = True
#     else:
#         is_sorted = False

# if is_sorted:
#     print("Sorted")
# else:
#     print("Not sorted")

# n = int(input("Enter the number for perfect number : "))
# sum_divisors = 0
# Divisors = []
# for i in range(1,n):
#     if n % i == 0:
#         sum_divisors = sum_divisors + i
#         Divisors += [i]
# if sum_divisors == n:
#     print(f"Divisors:{Divisors}\nSUM = {sum_divisors} → Perfect Number")
# else:
#     print(f"Divisors:{Divisors}\nSUM = {sum_divisors} → Not Perfect Number")

# list_input = [1, 2, 4, 5]

# for i in range(len(list_input)-1):
#     ind0 = list_input[i]
#     ind1 = list_input[i+1]
#     if (ind1 - ind0) > 1:
#         for missing in range(ind0+1,ind1):
#             print(missing)

# str_input = "I love Python"
# rev = ""
# word = ""
# for i in str_input:
#     if i != " ":
#         word =  i + word
#     else:
#         rev = rev + word + " "
#         word = ""
# rev += word
# print(rev)

# int_list =  [1, 2, 3, 5, 6]

# for i in range(len(int_list)-1):
#     ind0 = int_list[i]
#     ind1 = int_list[i+1]
#     if ind0 + 1 != ind1:
#         print(ind0+1)
#         break

# str_input = "madam"
# left = 0
# right = len(str_input) - 1

# is_palidrome = True

# while left < right:
#     if str_input[left] != str_input[right]:
#         is_palidrome = False
#         break
#     left += 1
#     right -= 1

# if is_palidrome:
#     print("Palidrome")
# else:
#     print("Not Palidrome")

# nums = [2, 1, 5, 1, 3, 2]
# k = 7

# left = 0
# current_sum = 0
# max_len = 0

# for right in range(len(nums)):
#     current_sum += nums[right]

#     while current_sum > k:
#         current_sum -= nums[left]
#         left += 1

#     max_len = max(max_len, right - left + 1)

# print(max_len)


