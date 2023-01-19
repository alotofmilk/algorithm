import sys
N = int(sys.stdin.readline().strip()); log = {}; now_company = {}
for i in range(N):
    status = (sys.stdin.readline()).split()
    log[status[0]] = status[1]
    if log[status[0]] == "enter": now_company[status[0]] = status[1]
    elif log[status[0]] == "leave": del now_company[status[0]]
result = sorted(now_company.keys(), reverse=True)
print(*result, sep="\n")