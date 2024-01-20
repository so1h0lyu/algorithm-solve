t = int(input())

for _ in range(t):
    result = input()
    l = len(result)
    total = 0
    current_score = 0
        
    for i in range(l):
        if result[i] == 'O':
            current_score += 1
        elif result[i] == 'X':
            current_score = 0
            
        total += current_score
    
    print(total)