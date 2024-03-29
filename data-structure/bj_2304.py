n = int(input())
pillars = []
area = 0

for i in range(n):
    position, height = map(int, input().split())
    pillars.append([position, height])

pillars.sort()

i = 0
for p in pillars:
    if p[1] > area:
        area = p[1]
        max_position = i
    i += 1

current = pillars[0][1]
for i in range(max_position):
    if current < pillars[i + 1][1]:
        area += (pillars[i + 1][0] - pillars[i][0]) * current
        current = pillars[i + 1][1]
    else:
        area += (pillars[i + 1][0] - pillars[i][0]) * current
        
current = pillars[-1][1]
for i in range(n - 1, max_position, -1):
    if current < pillars[i - 1][1]:
        area += (pillars[i][0] - pillars[i - 1][0]) * current
        current = pillars[i - 1][1]
    else:
        area += (pillars[i][0] - pillars[i - 1][0]) * current
        
print(area)