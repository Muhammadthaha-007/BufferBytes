def findDigits(n):
    digits = []
    og = n

    while og > 0:
        rem = og % 10
        digits.insert(0,rem)
        og //= 10
    count = 0
    for num in digits:
        if num == 0:
            pass
        elif n % num == 0:
            count += 1
    return count

print(findDigits(1012))
