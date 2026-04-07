n1 = int(input("Enter LCM number 1 :"))
n2 = int(input("Enter LCM number 2 :"))

biggest = 0

if n1 > n2:
    biggest += n1
else:
    biggest += n2

while True:
    if biggest % n1 == 0 and biggest % n2 == 0:
        lcm = biggest
        break
    biggest += 1
print(lcm)