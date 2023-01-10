T = int(input()); find_max = []
for i in range(T):
    numbers = list(map(int,input().split()))
    find_max.append(max(numbers))
for j in range(T): print("#{} {}".format(j+1, find_max[j]))