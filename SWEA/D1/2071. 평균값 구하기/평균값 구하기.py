T = int(input()); average = []; sum = 0
for i in range(T):
    numbers = list(map(int,input().split()))
    for j in range(10): sum += numbers[j]
    average.append(round(sum/10))
    numbers.clear(); sum = 0
for i in range(0,T): print("#{} {}".format(i+1, average[i]))