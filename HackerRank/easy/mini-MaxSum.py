
def miniMaxSum(arr):
    min_max = []
    if len(set(arr)) == 1:
        min_max.append(arr[0]*4)
    else:        
        arr_list = []
        for num in range(len(arr)):
            temp = []
            for ch in arr:
                temp.append(ch)
            arr_list.append(temp)

        main_list = []
        n = 0
        for num_list in arr_list:
            temp = []
            for ch in num_list:
                if ch == arr[n]:
                    num_list.remove(ch)
                    n += 1
                temp.append(ch)
            main_list.append(temp)
        if arr[0] in main_list[4]:
            main_list[4].remove(arr[0])
        
        for n_list in main_list:
            min_max.append(sum(n_list))
    return min(min_max), max(min_max)

print(miniMaxSum([5,5,5,5,5]))