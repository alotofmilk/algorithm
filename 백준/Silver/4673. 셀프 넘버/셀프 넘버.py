cnt = 1; self_num = [i for i in range(1, 10001)]
while cnt <= 10000:
    cnt_10000 = cnt // 10000; cnt_1000 = (cnt % 10000) // 1000; cnt_100 = (cnt % 1000) // 100; cnt_10 = (cnt % 100) // 10; cnt_1 = (cnt % 10)
    num = cnt + cnt_10000 + cnt_1000 + cnt_100 + cnt_10 + cnt_1
    if num in self_num: self_num.remove(num)
    cnt += 1
for i in range(len(self_num)): print(self_num[i], end="\n")