import sys
triangle = [int(sys.stdin.readline().strip()) for i in range(3)]
angle_sum = triangle[0] + triangle[1] + triangle[2]
if angle_sum != 180: print("Error")
else:
    if triangle[0] == triangle[1] and triangle[1] == triangle[2]:
        print("Equilateral")
    elif triangle[0] != triangle[1] and triangle[1] != triangle[2] and triangle[2] != triangle[0]:
        print("Scalene")
    else: print("Isosceles")