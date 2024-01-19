dishes = input()
l = len(dishes)
h = 0
current = ''

for i in range(0, l):
    if (dishes[i] == current):
        h += 5
    else:
        h += 10
    current = dishes[i]

print(h)