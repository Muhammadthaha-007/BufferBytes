def compareTriplets(a, b):
    res = []

    if len(a) == len(b):
        alise = 0
        bob = 0
        for ind in range(len(a)):
            if a[ind] < b[ind]:
                bob += 1
            elif a[ind] > b[ind]:
                alise += 1
            else:
                continue
        res.append(alise)
        res.append(bob)
    return res    

print(compareTriplets([5,6,7],[5,6,10]))