import sys

N = int(sys.stdin.readline()); result = []
for i in range(N):
    order = sys.stdin.readline().strip()
    if len(order) > 5:
        command, number = order.split(" "); number = int(number)
        result.append(number)
    else:
        if order == "pop":
            if len(result) > 0: print(result.pop())
            else: print(-1)
        elif order == "size": print(len(result))
        elif order == "empty":
            if len(result) == 0: print(1)
            else: print(0)
        elif order == "top":
            if len(result) > 0: print(result[len(result)-1])
            else: print(-1)