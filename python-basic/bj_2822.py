scores = []
sum = 0

for i in range(8):
    score = int(input())
    scores.append([i + 1, score])

scores.sort(key = lambda x: x[1])
del scores[0:3]

for i in range(5):
    sum += scores[i][1]

scores.sort(key = lambda x: x[0])

print(sum)
for i in range(5):
    print(scores[i][0], end = ' ')