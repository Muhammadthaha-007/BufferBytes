def solve(arr, queries):
    result = []
    for i in queries:
        sub = []
        for j in range(len(arr)-i+1):
            temp = arr[j:j+i]
            sub.append(max(temp))
        result.append(min(sub))
    return result
print(solve([33, 11, 44, 11, 55],[1, 2, 3, 4, 5]))
