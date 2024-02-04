k = int(input())
account = []
sum = 0

for _ in range(k):
    n = int(input())
    if (n != 0):
        account.append(n)
    else:
        account.pop()

for i in range(len(account)):
    sum += account[i]
    
print(sum)