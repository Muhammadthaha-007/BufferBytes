def arrayManipulation(n, queries):
    l_n = [0] * n
    for qur in queries:
        a, b, k = qur
        for ind in range(a-1,b):
            l_n[ind] += k
    return max(l_n)
print(arrayManipulation(5,[[1, 2, 100],[2, 5, 100],[3, 4, 100]]))