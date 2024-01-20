n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    ad_profit = e - c
    if r > ad_profit:
        print("do not advertise")
    elif r == ad_profit:
        print("does not matter")
    elif r < ad_profit:
        print("advertise")