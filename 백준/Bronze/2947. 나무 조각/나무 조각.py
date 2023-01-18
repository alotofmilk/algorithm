import sys
order = list(map(int,sys.stdin.readline().split()));
while True:
    for i in range(len(order)-1):
        if order[i] > order[i+1]:
            order[i], order[i+1] = order[i+1], order[i]
            print(*order)
        else: pass
    if order == [1,2,3,4,5]: break