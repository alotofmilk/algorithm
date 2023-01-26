import sys
import heapq
N = int(sys.stdin.readline())
card = [int(sys.stdin.readline().strip()) for i in range(N)]
heapq.heapify(card)
result = 0; sum_card = 0
if len(card) == 1: print(0)
else:
    while len(card) > 1:
        tmp1 = heapq.heappop(card)
        tmp2 = heapq.heappop(card)
        result = tmp1 + tmp2
        heapq.heappush(card, result)
        sum_card += result
    print(sum_card)