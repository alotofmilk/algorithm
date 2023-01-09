import sys
T = int(sys.stdin.readline()); iteration_list = []; sentence_list = []; new_sentence = ""
for i in range(T):
    R, S = map(str,sys.stdin.readline().split())
    iteration_list.append(int(R))
    sentence_list.append(S)
for i in range(0,T):
    for j in range(len(sentence_list[i])): new_sentence += iteration_list[i] * sentence_list[i][j]
    print(new_sentence)
    new_sentence = ""