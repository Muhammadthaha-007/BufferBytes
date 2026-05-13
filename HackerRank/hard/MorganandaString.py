def morganAndString(a, b):
    a = list(a)
    b = list(b)

    sl = []
    la = len(a)
    lb = len(b)

    for ind in range(la+lb):
        try:
            if a[0] < b[0]:
                sl.append(a[0])
                a.remove(a[0])
            elif a[0] > b[0]:
                sl.append(b[0])
                b.remove(b[0])
            else:
                sl.append(a[0])
                a.remove(a[0]) 
        except IndexError:
            break

    if a:
        sl += a
    elif b:
        sl += b

    fainal_str = ""
    for ch in sl:
        fainal_str += ch
    return fainal_str
print(morganAndString("ACA","BCF"))
