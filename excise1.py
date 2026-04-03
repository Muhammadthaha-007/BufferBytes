# string = "Python"
# rev = ""

# for i in string:
#     rev = i + rev

# print(rev)


count = 1
total_sum = 0

for i in range(1,601):
    if i % 14 == 0 and i % 21 == 0:
        print(f"sl.no {count} : {i}")
        total_sum += i
        count += 1

print(f"Count of number : {count-1}")
print(f"Total sum : {total_sum}")