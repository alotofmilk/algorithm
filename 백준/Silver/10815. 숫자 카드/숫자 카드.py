import sys
N = int(sys.stdin.readline()); cards = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline()); question = list(map(int,sys.stdin.readline().split()))
answer = {}
for i in range(len(cards)):
    answer[cards[i]] = 0
for i in range(len(question)):
    if question[i] not in answer.keys(): print(0, end = " ")
    else: print(1, end = " ")