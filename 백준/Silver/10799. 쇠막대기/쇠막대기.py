import sys
stick = sys.stdin.readline().strip()
stick = stick.replace("()","*"); stack = []; count = 0; sum = 0
for i in range(len(stick)):
    if stick[i] == "*": sum += count
    else:
        stack.append(stick[i])
        if stick[i] == "(": count += 1
        elif stick[i] == ")":
            count -= 1
            sum += 1
            stack.pop()
            stack.pop()
print(sum)