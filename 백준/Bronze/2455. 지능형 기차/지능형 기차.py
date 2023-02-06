import sys
station = [list(map(int,sys.stdin.readline().split())) for i in range(4)]
people_in_train = []
for i in range(4):
    if i == 0:
        people = station[i][1]
        people_in_train.append(people)
    elif 0 < i < 3:
        people = people_in_train[i-1] - station[i][0] + station[i][1]
        people_in_train.append(people)
    else:
        people = people_in_train[i-1] - station[i][0]
        people_in_train.append(people)
print(max(people_in_train))