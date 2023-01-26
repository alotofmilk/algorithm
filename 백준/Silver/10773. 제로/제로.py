import sys
K = int(sys.stdin.readline()); stack = []; result = 0
numbers = [int(sys.stdin.readline().strip()) for i in range(K)]
for i in range(K):
    if numbers[i] != 0:
        stack.append(numbers[i])
    else: stack.pop()
for i in range(len(stack)): result += stack[i]
print(result)