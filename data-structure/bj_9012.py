t = int(input())

for _ in range(t):
    ps = input()
    stack = []
    
    for i in range(len(ps)):
        stack.append(ps[i])
        
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
                
    if len(stack) == 0:
        print('YES')
    else:
        print('NO') 