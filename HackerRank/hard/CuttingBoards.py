def boardCutting(cost_y, cost_x):
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)

    total = 0
    x_count = 1
    y_count = 1

    i = 0
    j = 0

    while i < len(cost_y) and j < len(cost_x):
        if cost_y[i] >= cost_x[j]:
            total = total + cost_y[i] * x_count
            y_count += 1
            i += 1
        else:
            total = total + cost_x[j] * y_count
            x_count += 1
            j += 1
    while i < len(cost_y):
        total += cost_y[i] * x_count
        y_count += 1
        i += 1

    while j < len(cost_x):
        total += cost_x[j] * y_count
        x_count += 1
        j += 1
    
    return total % (10**9+7)
        
print(boardCutting([2, 1, 3, 1, 4],[4, 1, 2]))