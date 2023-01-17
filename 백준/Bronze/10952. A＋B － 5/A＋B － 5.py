import sys
answer = []
while True:
    A, B = map(int,sys.stdin.readline().split())
    if A == 0 and B == 0: break
    else: answer.append(A+B)
print(*answer, sep="\n")