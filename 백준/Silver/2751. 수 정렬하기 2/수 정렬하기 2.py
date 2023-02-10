import sys
import heapq
N = int(sys.stdin.readline()); result = []
numbers = [-int(sys.stdin.readline().strip()) for i in range(N)]
heapq.heapify(numbers)
numbers = sorted(numbers, reverse=True)
for i in range(N): print(-numbers[i])