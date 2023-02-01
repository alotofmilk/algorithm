import sys
T = int(sys.stdin.readline())

def judge(score_list):
    score_list = sorted(score_list); result = ""
    judge_sum = [score_list[1],score_list[2],score_list[3]]
    difference = [score_list[3]-score_list[2],score_list[3]-score_list[1],score_list[2]-score_list[1]]
    for i in range(len(difference)):
        if difference[i] >= 4:
            result = "KIN"
            break
        else: continue
    if result == "": result = sum(judge_sum)
    return result

for i in range(T):
    score_list = list(map(int,sys.stdin.readline().split()))
    answer = judge(score_list)
    print(answer)