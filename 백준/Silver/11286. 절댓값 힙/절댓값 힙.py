import sys
import heapq
N = int(sys.stdin.readline()); abs_heap = []
for i in range(N):
    number = int(sys.stdin.readline().strip())
    if number != 0: heapq.heappush(abs_heap, (abs(number),number))
    else:
        if len(abs_heap) == 0: print(0)
        else: print(heapq.heappop(abs_heap)[1])