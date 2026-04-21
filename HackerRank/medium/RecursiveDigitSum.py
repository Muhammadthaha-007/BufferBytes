def superDigit(n, k):
    if len(str(n)) == 1:
        return n
    sum_digits = sum([int(num) for num in str(n)]) * k
    
    return superDigit(sum_digits,1)

print(superDigit("123",3))