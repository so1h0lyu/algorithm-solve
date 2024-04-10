import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        if word in dict:
            dict[word][0] += 1
        else:
            dict[word] = [1, len(word), word]

result = sorted(dict.items(), key = lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in result:
    print(i[0])