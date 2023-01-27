import sys
import heapq
N = int(sys.stdin.readline()); result_heap = []; make_right_answer = []
for i in range(N):
    word = sys.stdin.readline().strip()
    alphabet_order = tuple([ord(word[i]) for i in range(len(word))])
    result = tuple([len(word)]) + alphabet_order + tuple([word])
    heapq.heappush(result_heap, result)
for i in range(N):
    answer = heapq.heappop(result_heap)[-1]
    if answer not in make_right_answer: make_right_answer.append(answer)
print(*make_right_answer, sep="\n")