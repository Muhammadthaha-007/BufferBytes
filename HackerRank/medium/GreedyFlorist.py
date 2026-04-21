def getMinimumCost(k, c):
    c.sort()
    c.reverse()
    length = len(c)
    result = []
    n = 1
    ind = 0
    for index in range(length):
        try:
            for people in range(k):
                result.append(c[ind]*n)
                ind += 1
            n += 1
        except IndexError:
            break

    return sum(result)
print(getMinimumCost(3,[1,2,3,4]))