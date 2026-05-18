def matrixRotation(matrix, r):
    rows = len(matrix)
    cols = len(matrix[0])

    total_layers = min(rows,cols) // 2
    layer_rings = []

    main_matrix = [[0] * cols for x in range(rows)]
    
    for layers in range(total_layers):
        rows_a = len(matrix)
        cols_a = len(matrix[0])
        
        top = []
        for x in matrix[0]:
            top.append(x)

        right = []
        for row in range(1,rows_a-1):
            right.append(matrix[row][cols_a-1])

        bottom = []
        for x in reversed(matrix[rows_a-1]):
            bottom.append(x)

        left = []
        for row in range(rows_a-2,0,-1):
            left.append(matrix[row][0])

        layer = top + right + bottom + left
        lgt_layer = len(layer)

        for rotation in range(r % lgt_layer):
            for ind in range(lgt_layer-1):
                layer[ind], layer[ind+1] = layer[ind+1], layer[ind]
        
        layer_rings.append(layer)
        
        del matrix[layers]

        for row in range(rows_a-2):
            matrix[row].remove(matrix[row][cols_a-1])
            matrix[row].remove(matrix[row][0])
   
        del matrix[rows_a-2]


    for lay in range(total_layers):
        n = 0

        top = lay
        bottom = rows - 1 - lay
        left = lay
        right = cols - 1 - lay

        try:
            for col in range(left, right + 1): 
                main_matrix[top][col] = layer_rings[lay][n]
                n += 1

            for row in range(top + 1, bottom):
                main_matrix[row][right] = layer_rings[lay][n]
                n += 1
                
            for col in range(right, left - 1, -1):
                main_matrix[bottom][col] = layer_rings[lay][n]
                n += 1
                
            for row in range(bottom - 1, top, -1):
                main_matrix[row][left] = layer_rings[lay][n]
                n += 1

        except IndexError:
            break
                
    for row in main_matrix:
        for col in row:
            print(col,end=" ")
        print()
    return 
print(matrixRotation([[1, 2, 3, 4], [5,6,7,8],[9,10,11,12],[13,14,15,16]],2))