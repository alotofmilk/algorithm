import sys
W_score = []; K_score = []
for i in range(20):
    score = int(sys.stdin.readline().strip())
    if i < 10: W_score.append(score)
    else: K_score.append(score)
W_score = sorted(W_score, reverse=True); K_score = sorted(K_score, reverse=True)
W_result = W_score[0] + W_score[1] + W_score[2]
K_result = K_score[0] + K_score[1] + K_score[2]
print(W_result, K_result, sep = " ")