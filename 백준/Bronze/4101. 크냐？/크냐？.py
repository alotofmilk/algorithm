import sys
result = []
while True:
    A, B = map(int,sys.stdin.readline().split())
    if A == 0 and B == 0: break
    else:
        if A <= B: result.append("No")
        else: result.append("Yes")
print(*result, sep="\n")