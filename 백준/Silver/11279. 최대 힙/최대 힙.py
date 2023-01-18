import heapq
import sys

N = int(sys.stdin.readline()); numbers = []; min_heap = [];
for i in range(N): numbers.append(int(sys.stdin.readline()))
for i in range(N):
    if numbers[i] == 0:
        if len(min_heap) == 0: print(0)
        else: print(-heapq.heappop(min_heap))
    else: heapq.heappush(min_heap, -numbers[i])