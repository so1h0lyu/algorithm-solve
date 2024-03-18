n = int(input())
count = 0

for _ in range(n):
    word = input()
    stack = []
    
    for i in range(len(word)):
        stack.append(word[i])
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
    if len(stack) == 0:
        count += 1  
        
print(count)