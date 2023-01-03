h, m = input().split()
H = int(h)
M = int(m)

if M >= 45:
    print("{} {}".format(H, M-45))
elif M < 45:
    if H != 0:
        H = H - 1
        M = M + 60
        print("{} {}".format(H, M-45))
    elif H == 0:
        H = 23
        M = M + 60
        print("{} {}".format(H, M-45))