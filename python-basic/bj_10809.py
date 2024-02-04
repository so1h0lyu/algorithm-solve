s = input()
count = []
for i in range(97, 123):
    count.append([i, -1])

for i in range(len(s)):
    for j in range(len(count)):
        if (ord(s[i]) == count[j][0]):
            if (count[j][1] == -1):
                count[j][1] = i

for i in range(len(count)):
    print(count[i][1], end = ' ')