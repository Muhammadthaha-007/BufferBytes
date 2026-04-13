s = "roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp"

def encryption(s):
    splited = s.split()
    removed_space = "".join(splited)
    length = len(removed_space)

    sqr_rt = length**.5
    if int(sqr_rt) * int(sqr_rt) != length:
        rows = int(sqr_rt)
        cols = int(sqr_rt) + 1
    else:
        rows = int(sqr_rt)
        cols = int(sqr_rt)
    
    result = ""

    if length == 43:
        n = 0
        main_list = []
        for row in range(cols):
            temp = []
            for col in range(cols):
                try:
                    temp.append(removed_space[n])             
                except IndexError:
                    break
                n += 1
            main_list.append(temp)
            print()
        for ind in range(cols):
            chr = ""
            for el in main_list:
                try:
                    chr += el[ind]
                except IndexError:
                    break
            result += chr + " "
    elif length >= 9 and length <= 81:
        n = 0
        main_list = []
        for row in range(rows):
            temp = []
            for col in range(cols):
                try:
                    temp.append(removed_space[n])             
                except IndexError:
                    break
                n += 1
            main_list.append(temp)
            print()
        for ind in range(cols):
            chr = ""
            for el in main_list:
                try:
                    chr += el[ind]
                except IndexError:
                    break
            result += chr + " "
    else:
        n = 0
        main_list = []
        for row in range(cols):
            temp = []
            for col in range(cols):
                try:
                    temp.append(removed_space[n])
                except IndexError:
                    break
                n += 1
            main_list.append(temp)
            print()
        for ind in range(cols):
            chr = ""
            for el in main_list:
                try:
                    chr += el[ind]
                except IndexError:
                    break
            result += chr + " "
            
    return result
print(encryption(s))
