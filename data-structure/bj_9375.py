t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    count = 1
    
    for i in range(n):
        name, kind = input().split()
        if i == 0:
            clothes[kind] = 1
        else:
            if kind in clothes:
                clothes[kind] += 1
            else:
                clothes[kind] = 1
        
    for key in clothes:
        count *= clothes[key] + 1
    
    print(count - 1)