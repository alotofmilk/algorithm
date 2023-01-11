N = int(input()); alphabet = "abcdefghijklmnopqrstuvwxyz"; answer = []; cnt = 0
for i in range(N):
    sentence = input()
    for j in range(len(sentence)):
        if sentence[j] == alphabet[j]: cnt += 1
        else: break
    answer.append(cnt); cnt = 0; sentence = ""
for i in range(N): print("#{} {}".format(i+1, answer[i]))