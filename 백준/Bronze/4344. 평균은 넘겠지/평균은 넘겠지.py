import sys
C = int(sys.stdin.readline())
student_result = [sys.stdin.readline().strip() for i in range(C)]
result_matrix = []
sum = 0
average = 0
cnt = 0
for i in range(0,C):
    result_matrix = student_result[i].split(" ")
    for j in range(1,len(result_matrix)):
        sum += int(result_matrix[j])
    average = sum / int(result_matrix[0])
    for j in range(1,len(result_matrix)):
        if int(result_matrix[j]) > average:
            cnt += 1
        else:
            pass
    print(f'{cnt / int(result_matrix[0]) * 100 :.3f}%')
    result_matrix.clear()
    sum = 0
    average = 0
    cnt = 0