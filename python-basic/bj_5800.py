k = int(input())

for i in range(k):
    n = list(map(int, input().split()))
    n.pop(0)
    n.sort(reverse = True)
    max = n[0]
    min = n[len(n) - 1]
    
    gap = 0
    for j in range(0, len(n) - 1):
        if (gap < (n[j] - n[j + 1])):
            gap = n[j] - n[j + 1]
    
    print("Class", i + 1)
    print("Max {}, Min {}, Largest gap {}".format(max, min, gap))