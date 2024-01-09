import sys
dot_list = []
for i in range(0,3):
    a, b = map(int,sys.stdin.readline().split())
    dot_list.append([a,b])

x_list = [dot_list[0][0], dot_list[1][0], dot_list[2][0]]
y_list = [dot_list[0][1], dot_list[1][1], dot_list[2][1]]
answer_x = 0; answer_y = 0

if x_list.count(dot_list[0][0]) == 1:
    answer_x = dot_list[0][0]
else:
    if x_list.count(dot_list[1][0]) == 1:
        answer_x = dot_list[1][0]
    else:
        answer_x = dot_list[2][0]

if y_list.count(dot_list[0][1]) == 1:
    answer_y = dot_list[0][1]
else:
    if y_list.count(dot_list[1][1]) == 1:
        answer_y = dot_list[1][1]
    else:
        answer_y = dot_list[2][1]

print(answer_x, answer_y)