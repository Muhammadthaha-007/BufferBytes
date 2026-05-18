def matrixRotation(matrix, r):
    rows = len(matrix)
    cols = len(matrix[0])

    total_layers = min(rows,cols) // 2

    for lay in range(total_layers):

        n = 0

        top = lay
        bottom = rows - 1 - lay
        left = lay
        right = cols - 1 - lay

        top_ar = []
        for col in range(left, right + 1): 
            top_ar.append(matrix[top][col])

        right_ar = []
        for row in range(top + 1, bottom):
            right_ar.append(matrix[row][right])

        bottom_ar = []
        for col in range(right, left - 1, -1):
            bottom_ar.append(matrix[bottom][col])

        left_ar = []
        for row in range(bottom - 1, top, -1):
            left_ar.append(matrix[row][left])

        layer = top_ar + right_ar + bottom_ar + left_ar
        lgt_layer = len(layer)

        for rotation in range(r % lgt_layer):
            for ind in range(lgt_layer-1):
                layer[ind], layer[ind+1] = layer[ind+1], layer[ind]

        for col in range(left, right + 1): 
            matrix[top][col] = layer[n]
            n += 1

        for row in range(top + 1, bottom):
            matrix[row][right] = layer[n]
            n += 1
            
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = layer[n]
            n += 1
            
        for row in range(bottom - 1, top, -1):
            matrix[row][left] = layer[n]
            n += 1
                
    for row in matrix:
        for col in row:
            print(col,end=" ")
        print()
    return 
print(matrixRotation([[1, 2, 3, 4], [7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]],7))