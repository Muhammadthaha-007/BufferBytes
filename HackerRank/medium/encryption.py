s = "chillout"

def encryption(s):
    splited = s.split()
    removed_space = "".join(splited)
    length = len(removed_space)

    sqr_rt = length**.5
    rows = int(sqr_rt)
    cols = rows + 1
    
    result = ""

    if length >= 9:
        n = 0
        for row in range(rows):
            for col in range(cols):
                if n != length:
                    print(removed_space[n],end="")
                else:
                    break
                n += 1
            print()
    else:
        n = 0
        for row in range(cols):
            for col in range(cols):
                if n != length:
                    print(removed_space[n],end="")
                else:
                    break
                n += 1
            print()
    return length
print(encryption(s))
