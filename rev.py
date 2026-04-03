# string = input("Enter a String: ")
# rev = ""
# for i in string:
#     rev = i + rev
# print("Reversed String is:", rev)


data_range = int(input("Enter the data Range : "))
data = []
odd_data = []
even_data = []
if data_range < 2:
    print("OOPS! at least 2 length neede !")
else:
    for i in range(data_range):
        try:
            num = int(input(f"Enter the item no.{i+1}: "))
            data.append(num)
        except ValueError:
            print(f"You have been skipped item sl.no :{i+1}  !")
    for even in data:
        if even % 2 != 0:
            odd_data.append(even)
        else:
            even_data.append(even)
    even_sorted_set = sorted(set(even_data))
    odd_sorted_set = sorted(set(odd_data))
    if len(even_sorted_set) == 1:
        print(f"All Even are same data = {even_sorted_set[0]}")
    if len(odd_sorted_set) == 1:
        print(f"All Odd are same data = {odd_sorted_set[0]}")
    if not odd_data:
        print("No odd data found !")
        if even_data:
            print(f"Even data : {even_data}")
            if len(even_sorted_set) != 1:
                print(f"Smallest even : {even_sorted_set[0]}")
                print(f"Second Smallest even : {even_sorted_set[1]}")
                print(f"Largest even : {even_sorted_set[-1]}")
                print(f"Second largest even : {even_sorted_set[-2]}")
    if not even_data:
        print("No even data found !")
        if odd_data:
            print(f"Odd data : {odd_data}")
            if len(odd_sorted_set) != 1:
                print(f"Smallest odd : {odd_sorted_set[0]}")
                print(f"Second Smallest odd : {odd_sorted_set[1]}")
                print(f"Largest odd : {odd_sorted_set[-1]}")
                print(f"Second Largest odd : {odd_sorted_set[-2]}")
    elif even_data and odd_data:
        print("--------------START------------------")
        print(f"Odd data : {odd_data}")
        if len(odd_sorted_set) != 1:
            print(f"Smallest odd : {odd_sorted_set[0]}")
            print(f"Second Smallest odd : {odd_sorted_set[1]}")
            print(f"Largest odd : {odd_sorted_set[-1]}")
            print(f"Second Largest odd : {odd_sorted_set[-2]}")
        print("-------------------------------------")
        print(f"Even data : {even_data}")
        if len(even_sorted_set) != 1:
            print(f"Smallest even : {even_sorted_set[0]}")
            print(f"Second Smallest even : {even_sorted_set[1]}")
            print(f"Largest even : {even_sorted_set[-1]}")
            print(f"Second largest even : {even_sorted_set[-2]}")
        print("---------------END--------------------")