cnt = 0
for i in range(0,5):
    for j in range(0,5):
        if cnt == j: print("#",end="")
        else: print("+",end="")
    cnt += 1
    print("")