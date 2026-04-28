def minimumPasses(m, w, p, n):
    count = 1
    candies = m * w
    while candies <= n:
        if candies >= p:
            p_count = candies // p
            if m > w:
                w = p_count * p
            elif m < w:
                m = p_count * p
            count += 1
        candies = m * w

    return count

print(minimumPasses(3,1,2,12))