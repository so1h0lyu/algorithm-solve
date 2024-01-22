import math

m = int(input())
n = int(input())
sum = 0

for i in range(m, n + 1):
    if math.sqrt(i) % 1 == 0:
        if sum == 0:
            min = i
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)