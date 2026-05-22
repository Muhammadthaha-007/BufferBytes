def morganAndString(a, b):
    res = ""
    while a and b:
        if a < b:
            res += a[0]
            a = a[1:]
        else:
            res += b[0]
            b = b[1:]

    return res+a+b
print(morganAndString("ACA","BCF"))
