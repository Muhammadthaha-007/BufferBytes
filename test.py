# for i in range(0,6):
#     for j in range(0,i+1):
#         print("*", end="")
#     print("")



# for i in range(0,5):
#     for k in range(i+1,6):
#         print(k-i, end="")
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# row=6    
# for i in range(1,row):
#     for j in range(1,row-i+1):
#         print(j, end="")
#     for k in range(1,i):
#         print("*", end="")
#     print()


# l = [5,6,2,4,3,1]
# s = []

# for i in l :
     

# x = int(input("enter a nbr :"))

# row=5
# stars = 8
# for i in range(1,row):
#     for j in range(1,stars+1):
#         if i == 2 and j in [3,4]:
#             print(" ", end="")
#         elif i == 3  and j in [3,4,5,6]:
#             print(" ", end="")
#         elif i == 4  and j in [2,3,4,5,6,7]:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()
#     stars -= 2

# row = 5
# stars = 8  # starting with 8 stars in the first row

# for i in range(1, row):
#     total = stars - (i - 1) * 2
#     for j in range(1, total + 1):
#         if i == 2 and j in [3, 4]:
#             print(" ", end="")
#         elif i == 3 and j in [3, 4, 5, 6]:
#             print(" ", end="")
#         elif i == 4 and j in [2, 3, 4, 5, 6, 7]:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()


x = int(input("Enter the number"))
result = 1

for i in range(1, x+1):
    result *= i
print("Factorial of", x, "is", result)