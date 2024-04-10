import sys

numbers = list(map(str, sys.stdin.readline().strip()))

pointer = 0
i = 1
while pointer < len(numbers):
    temp = str(i)
    
    for j in range(len(temp)):
        if pointer >= len(numbers):
            break
        if temp[j] == numbers[pointer]:
            pointer += 1
            
    i += 1
    
print(i - 1)