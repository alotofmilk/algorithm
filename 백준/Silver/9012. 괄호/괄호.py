import sys
T = int(sys.stdin.readline()); sentence = []; stack = []
for i in range(T):
    sentence.append(sys.stdin.readline().strip())
    for j in range(len(sentence[i])):
        if sentence[i][j] == "(": stack.append(sentence[i][j])
        elif sentence[i][j] == ")":
            if len(stack) > 0: stack.pop()
            else:
                stack.append(sentence[i][j])
                break
    if len(stack) == 0:
        print("YES")
        stack.clear()
    else:
        print("NO")
        stack.clear()