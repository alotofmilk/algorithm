def solution(num_list, n):
    answer = []; cnt = 0
    while(cnt < len(num_list)):
        answer.append(num_list[cnt])
        cnt += n
    return answer