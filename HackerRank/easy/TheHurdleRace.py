def hurdleRace(k, height):
    tallest_hurdle = max(height)
    if k > tallest_hurdle:
        return 0
    else:
        return tallest_hurdle - k

print(hurdleRace(1, [1,2,3,3,2]))