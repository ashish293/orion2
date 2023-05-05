num = int(input())

for i in range(1, num):
    print(" "*(i-1) + str(i) + "  "*(num-i) + str(i))
print((num-1)*" " + str(num))

for i in range(num-1, 0, -1):
    print(" "*(i-1) + str(i) + "  "*(num-i) + str(i))
