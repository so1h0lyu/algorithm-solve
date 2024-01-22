n = int(input())
score = list(input().split())
max = 0
sum = 0

for i in range(n):
    score[i] = int(score[i])
    if max < score[i]:
        max = score[i]

for i in range(n):
    sum += score[i] / max * 100
    
average = sum / n
print(average)