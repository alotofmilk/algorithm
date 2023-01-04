x = input()
X = int(x)
n = input()
N = int(n)

total_purchase = 0
price = []
how_many = []

for i in range(0,N):
    A, B = input().split()
    a = int(A)
    price.append(a)
    b = int(B)
    how_many.append(b)
    
for i in range(0,N):
    total_purchase += price[i] * how_many[i]

if X == total_purchase:
    print("Yes")
else:
    print("No")