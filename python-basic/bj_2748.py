n = int(input())
fibonachi = [0, 1]

for i in range(2, n + 1):
    fibonachi.append(fibonachi[i - 1] + fibonachi[i - 2])

print(fibonachi[n])