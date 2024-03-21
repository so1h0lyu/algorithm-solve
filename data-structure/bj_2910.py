n, c = map(int, input().split())
numbers = list(map(int, input().split()))
dict = {}

for number in numbers:
    if number in dict.keys():
        dict[number] += 1
    else:
        dict[number] = 1
    
dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)

for pairs in dict:
    for _ in range(pairs[1]):
        print(pairs[0], end = ' ')