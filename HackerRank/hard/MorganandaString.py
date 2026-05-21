def morganAndString(a, b):
    res = ""
    while a and b:
        if a < b:
            res += a[0]
            a = a[1:]
        else:
            if a[0] < b[0]:
                res += a[0]
                a = a[1:]
            else:
                res += b[0]
                b = b[1:]

    return res+a+b
print(morganAndString("ACA","BCF"))




    # a = list(a)
    # b = list(b)

    # sl = []
    # la = len(a)
    # lb = len(b)

    # for ind in range(la+lb):
    #     try:
    #         if a[0] < b[0]:
    #             sl.append(a[0])
    #             a.remove(a[0])
    #         elif a[0] > b[0]:
    #             sl.append(b[0])
    #             b.remove(b[0])
    #         else:
    #             sl.append(a[0])
    #             a.remove(a[0]) 
    #     except IndexError:
    #         break

    # if a:
    #     sl += a
    # elif b:
    #     sl += b

    # fainal_str = ""
    # for ch in sl:
    #     fainal_str += ch
        
    # return fainal_str




