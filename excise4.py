#here is my code >

count = 0
total_sum = 0

for i in range(1,3001):
    if i % 28 == 0 and i % 32 == 0:
        print(f"{i}")
        count += 1
        total_sum += i

print(f"Matched Numbers : {count}")
print(f"Total Sum : {total_sum}")