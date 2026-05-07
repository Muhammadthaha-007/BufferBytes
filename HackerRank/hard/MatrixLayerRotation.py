def matrixRotation(matrix, r):
    col = len(matrix[0])
    row = len(matrix)

    outer_layer = []
    last_row = []

    inner_layer = []

    for rows in range(row):
        for colm in range(col):
            if rows == 0 or rows == row-1:
                if rows == row-1:
                    last_row.insert(0,matrix[rows][colm])
                else:
                    outer_layer.append(matrix[rows][colm])
            else:
                outer_layer.append(matrix[rows][col-1])
                break
    outer_layer += last_row
    for indx in range(row-2,0,-1):
        outer_layer.append(matrix[indx][0])
        
    for rotation in range(r):
        for index in range(len(outer_layer)):
            try:
                outer_layer[index], outer_layer[index+1] = outer_layer[index+1], outer_layer[index]
            except IndexError:
                break
    for rows in range(row):
        for colm in range(col):
            if rows > 0 and rows < row-1:
                if colm != 0 and colm != col-1:
                    if rows > 1:
                        inner_layer.insert(rows,matrix[rows][colm])
                    else:
                        inner_layer.append(matrix[rows][colm])
    for rotation in range(r):
        for ind in range(len(inner_layer)):
            try:
                inner_layer[ind], inner_layer[ind+1] = inner_layer[ind+1], inner_layer[ind]
            except IndexError:
                break

    main_matrix = []
    n = 0
    for length in range(len(matrix)+1):
        rows = []
        for lgt in range(len(matrix[0])):
            try:
                if length > 0 and length < len(matrix)-1:
                    rows.append(outer_layer[n])
                    n += 1
                    break
                else:
                    if length == row-1:
                        rows.insert(0,outer_layer[n]) 
                    else:  
                        rows.append(outer_layer[n])
                    n += 1
            except IndexError:
                break
        main_matrix.append(rows)
    main_matrix[len(main_matrix)-1].reverse()
    j = 0
    for indxx in range(1,len(main_matrix[len(main_matrix)-1])+1):
        main_matrix[indxx].insert(0,main_matrix[len(main_matrix)-1][j])
        j += 1
        
    main_matrix.pop()
    
    
    return main_matrix
print(matrixRotation([[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],2))