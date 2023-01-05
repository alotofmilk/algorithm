import sys
N = int(sys.stdin.readline())
score_list = list(map(int,sys.stdin.readline().split()))
find_max = max(score_list)
modify_score = [score_list[i] / find_max * 100 for i in range(0,len(score_list))]
new_average = lambda list: print(sum(list) / len(list))
new_average(modify_score)