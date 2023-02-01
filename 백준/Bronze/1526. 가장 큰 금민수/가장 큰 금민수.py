import sys
N = int(sys.stdin.readline()); number = 1; flag = 0; result = []
while number <= N:
    number = str(number)
    for i in range(len(number)):
        if str(number[i]) == "4" or str(number[i]) == "7": pass
        else:
            flag = 1
            break
    number = int(number)
    if flag == 0: result.append(number)
    number += 1
    flag = 0
print(max(result))