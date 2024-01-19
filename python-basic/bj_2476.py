n = int(input())
max_prise = 0

for i in range(n):
    one, two, three = map(int, input().split())
    if (one == two) & (two == three):
        prise = 10000 + (one * 1000)
    elif (one == two) | (one == three):
        prise = 1000 + (one * 100)
    elif (two == three):
        prise = 1000 + (two * 100)
    else:
        max_number = max(one, two, three)
        prise = max_number * 100
    
    if max_prise < prise:
        max_prise = prise
        
print(max_prise)