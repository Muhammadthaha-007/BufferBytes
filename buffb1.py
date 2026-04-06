# rows = 5

# for upper in range(rows):
#     for col in range(upper):
#         if upper % 2 != 0 and col % 2 == 0:
#             print("*",end=" ")
#         elif upper % 2 == 0 and col % 2 != 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for lower in range(rows):
#     for col in range(rows - lower):
#         if lower % 2 == 0 and col % 2 == 0:
#             print("*",end=" ")
#         elif lower % 2 != 0 and col % 2 != 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# rows = int(input("Enter the row :"))
# temp_a = rows
# n = temp_a
# for row in range(rows*2):
#     for col in range(row+1):
#         if row > temp_a and col == n:
#             print(" ",end=" ")
#             n -= 1
#         elif row > temp_a and col > n:
#             print(" ",end="")
#         elif row % 2 == 0 and col % 2 != 0 or row % 2 != 0 and col % 2 == 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")  
#     print()


n = 2142

digits = []

while n > 0:
    rem = n % 10
    digits.insert(0,rem)
    n //= 10

rows = max(digits) + 1
cols = len(digits)

for row in range(rows):
    for col in range(cols):
        if row == 0:
            print(digits[col],end=" ")
        elif col == (cols-cols) and row in [x for x in range(1,rows-digits[0])]:
            print(" ",end=" ")
        elif col == 1 and row in [x for x in range(1,rows-digits[1])]:
            print(" ",end=" ")
        elif col == 2 and row in [x for x in range(1,rows-digits[2])]:
            print(" ",end=" ")
        elif col == 3 and row in [x for x in range(1,rows-digits[3])]:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()