import sys
n = int(sys.stdin.readline()); stack = []; answer = []; flag = 0; cur = 1
for i in range(n):
    number = int(sys.stdin.readline().strip())
    while cur <= number:
        stack.append(cur)
        answer.append("+")
        cur += 1
    if stack[-1] == number:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in range(len(answer)): print(answer[i])