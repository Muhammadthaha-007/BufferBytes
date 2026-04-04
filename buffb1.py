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

rows = 5
print("--Play Button--")

for row in range(rows*2-1):
    for col in range(rows):
        if row == 0 and col == 0 or\
             row == 1 and col == 1 or\
                 row == 2 and col in [0,2] or\
                    row == 3 and col in [1,3] or\
                         row == 4 and col in [0,2,4] or\
                             row == 5 and col in [1,3] or\
                                row == 6 and col in [0,2] or\
                                     row == 7 and col == 1 or\
                                         row == 8 and col == 0:
                                         print("*",end=" ")
        else:
            print(" ",end=" ")

    print()