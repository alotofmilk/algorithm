import sys
N = int(sys.stdin.readline())
height = list(map(int,sys.stdin.readline().split()))
flag = 0; before = height[0]; first = 0; last = 0; result = []
for i in range(1,N):
    if height[i] > before:
        if first == 0: first = height[0]
        last = height[i]
        before = height[i]
        result.append(last-first)
    else:
        result.append(last-first)
        before = height[i]
        first = height[i]
        last = 0
print(max(result))