t = int(input())

for i in range(t):
    n = int(input())
    max = 0
    
    for j in range(n):
        univ, scale = input().split()
        
        if int(scale) > max:
            max = int(scale)
            max_univ = univ
        
    print(max_univ)