import sys
M = int(sys.stdin.readline())
cup = [1, 2, 3]; change_cnt = 1; result = 0
while change_cnt <= M:
    X, Y = map(int,sys.stdin.readline().split())
    if X in cup and Y in cup:
        index_X = cup.index(X)
        index_Y = cup.index(Y)
        cup[index_X], cup[index_Y] = cup[index_Y], cup[index_X]
    result = cup[0]
    change_cnt += 1
print(result)