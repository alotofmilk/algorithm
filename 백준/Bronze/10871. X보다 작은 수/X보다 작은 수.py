import sys
N, X = map(int, sys.stdin.readline().split())
numbers = []
cnt = []
numbers = list(map(int,sys.stdin.readline().split()))
for i in range(len(numbers)):
    if numbers[i] < X:
        cnt.append(numbers[i])
print(*cnt)