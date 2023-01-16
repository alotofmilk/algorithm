import sys
N = int(sys.stdin.readline())
results = list(map(int,sys.stdin.readline().split())); cnt = 0; score = 0
for i in range(N):
    if results[i] == 1:
        cnt += 1
        score += cnt
    else: cnt = 0
print(score) 