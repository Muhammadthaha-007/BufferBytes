
def miniMaxSum(arr):
    arr_list = []
    for num in range(len(arr)):
        temp = []
        for ch in arr:
            temp.append(ch)
        arr_list.append(temp)

    main_list = []
    n = 4
    for num_list in arr_list:
        temp = []
        for ch in num_list:
            if ch == arr[n]:
                num_list.remove(ch)
                n -= 1
                print(n)
            temp.append(ch)
        main_list.append(temp) 

    return main_list

print(miniMaxSum([1,3,5,7,9]))