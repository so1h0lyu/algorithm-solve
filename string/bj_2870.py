import re
numbers = []
result = []

n = int(input())
for i in range(n):
    string = input()
    find_numbers = re.findall(r'\d+', string)
    numbers.extend(find_numbers)

for number in numbers:
    for i in range(len(number)):
        if len(number) > 1:
            if number[0] == '0':
                number = number[1:]
    result.append(int(number))

result.sort()
for i in result:
    print(i)