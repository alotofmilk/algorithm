import sys
N = int(sys.stdin.readline())
height = [int(sys.stdin.readline().strip()) for i in range(N)]
compare = height[-1]; result = 1
for i in range(N-1,-1,-1):
    if height[i] > compare:
        compare = height[i]
        result += 1
    else: pass
print(result)