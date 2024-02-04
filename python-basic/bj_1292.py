array = []
current = 1
sum = 0

for i in range(1, 1000):
    for j in range(current):
        array.append(current)
    current += 1
    
a, b = map(int, input().split())

for i in range(a - 1, b):
    sum += array[i]
    
print(sum)