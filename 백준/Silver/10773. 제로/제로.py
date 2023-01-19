import sys
K = int(sys.stdin.readline()); result = []
for i in range(K):
    money = int(sys.stdin.readline().strip())
    if money != 0: result.append(money)
    else: result.pop()
print(sum(result))