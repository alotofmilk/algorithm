import sys
students, winner = map(int,sys.stdin.readline().split())
score = list(map(int,sys.stdin.readline().split()))
score = sorted(score,reverse=True)
print(score[winner-1])