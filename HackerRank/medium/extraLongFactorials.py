# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(30))

def extraLongFactorials(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    print(res)
