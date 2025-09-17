# 반복문(for)
# 구구단

for x in range(2,10): # 2 -> 9
    for y in range(1,10): # 1 -> 9
        print("%2d" % (x * y), end=' ')
    print('')