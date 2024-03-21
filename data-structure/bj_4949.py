while (True):
    string = input()
    stack = []
    
    if string == ".":
        break
        
    for i in range(len(string)):
        if string[i] == '(' or string[i] == ')' or string[i] == '[' or string[i] == ']':
            stack.append(string[i])
            
            if len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                    
                elif stack[-1] == ']' and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
            
    if len(stack) == 0:
        print("yes")
    else:
        print("no")