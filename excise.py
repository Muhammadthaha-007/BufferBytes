rolling_range = int(input("Enter The Rolling Range :"))
con = 1
for i in range(1,rolling_range+1):
    
    print(f"Rolling : {con}")

    n = int(input("Enter The Number : "))

    original_num = n
    rev = 0
    count = 0

    while n > 0:
        reminder = n % 10
        rev = rev * 10 + reminder
        n = n // 10
        count += 1

    x = "Palidrome :"
    print(f"Reversed Number : {rev}")
    print(f"Digitz Count : {count}")
    if original_num == rev:
        print(f"{x} Yes")
    else:
        print(f"{x} No")

    con += 1