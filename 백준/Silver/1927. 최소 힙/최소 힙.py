import heapq
import sys
N = int(sys.stdin.readline());
min_heap = []
for i in range(N):
    number = int(sys.stdin.readline())
    if number > 0:
        heapq.heappush(min_heap,number)
    else:
        if len(min_heap) == 0: print(0)
        else:
            min_number = heapq.heappop(min_heap)
            print(min_number)