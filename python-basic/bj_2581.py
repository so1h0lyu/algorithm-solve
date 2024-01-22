def prime(n):
    if n == 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

m = int(input())
n = int(input())
sum = 0

for i in range(m, n + 1):
    if prime(i) == True:
        if sum == 0:
            min = i
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)