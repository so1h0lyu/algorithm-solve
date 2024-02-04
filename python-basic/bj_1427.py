number = input()
n = list(map(int, number))
n.sort(reverse = True)

for i in range(len(n)):
    print(n[i], end = '')