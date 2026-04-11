def staircase(n):
    rows = n

    for row in range(1,rows+1):
        for blank in range(rows-row):
            print(" ",end="")
        for col in range(row):
            print("#",end="")
        print()

staircase(6)