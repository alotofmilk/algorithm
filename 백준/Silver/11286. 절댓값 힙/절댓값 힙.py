import heapq
import sys

N = int(sys.stdin.readline()); numbers = []; result = []
for i in range(N): numbers.append(int(sys.stdin.readline()))
for i in range(N):
    if numbers[i] == 0:
        if len(result) == 0: print(0)
        else: print(heapq.heappop(result)[1])
    elif numbers[i] != 0: heapq.heappush(result, (abs(numbers[i]), numbers[i]))