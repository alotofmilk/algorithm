import sys
problem_stack = []
while True:
    sentence = sys.stdin.readline().strip()
    if sentence == "고무오리 디버깅 시작": pass
    elif sentence == "문제": problem_stack.append("문제")
    elif sentence == "고무오리":
        if len(problem_stack) != 0: problem_stack.pop()
        else:
            problem_stack.append("문제")
            problem_stack.append("문제")
    elif sentence == "고무오리 디버깅 끝": break
if len(problem_stack) == 0: print("고무오리야 사랑해")
else: print("힝구")