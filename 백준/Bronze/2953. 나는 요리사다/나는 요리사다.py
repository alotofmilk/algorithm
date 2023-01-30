import sys
import heapq

score_matrix = []; result = []; sum = 0
for i in range(5):
    line = list(map(int, sys.stdin.readline().split()))
    score_matrix.append(line)
    for j in range(4): sum += score_matrix[i][j]
    heapq.heappush(result, (-sum, i+1))
    sum = 0
winner_score = result[0][0]
winner = result[0][1]
print(winner, -winner_score, sep = " ")