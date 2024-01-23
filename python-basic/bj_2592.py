number = []
count = {}
sum = 0
max_count = 0

for i in range(10):
    number.append(int(input()))
    sum += number[i]
    
average = int(sum / 10)

for i in range(10):
    if number[i] in count.keys():
        count[number[i]] += 1
    else:
        count[number[i]] = 1

for num in count.keys():
    if max_count < count[num]:
        max = num
        max_count = count[num]
        
print(average)
print(max)