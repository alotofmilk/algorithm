import sys
import heapq
A, B, C = map(int,sys.stdin.readline().split()); min_heap = []
heapq.heappush(min_heap,A); heapq.heappush(min_heap,B); heapq.heappush(min_heap,C)
heapq.heappop(min_heap)
print(min_heap[0])