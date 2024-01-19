point1 = input().split()
point2 = input().split()
point3 = input().split()

if (point1[0] == point2[0]):
    x = point3[0]
else:
    if (point1[0] == point3[0]):
        x = point2[0]
    else:
        x = point1[0]

if (point1[1] == point2[1]):
    y = point3[1]
else:
    if (point1[1] == point3[1]):
        y = point2[1]
    else:
        y = point1[1]
        
print("{} {}".format(x, y))