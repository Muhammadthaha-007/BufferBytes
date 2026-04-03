n = 587

input_num = n
digits_list = []
sumOf_digits = 0

while n > 0:
    digits = n % 10
    digits_list.insert(0,digits)
    sumOf_digits += digits
    n = n // 10

print(f"Input : {input_num}")

for i in digits_list:
    print(f"digits :{i}", end=" ")
print()

print(f"Sum : {sumOf_digits}")