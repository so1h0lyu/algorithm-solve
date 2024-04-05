player = {}
result = ""
n = int(input())

for i in range(n):
    name = input()
    if name[0] in player:
        player[name[0]] += 1
    else:
        player[name[0]] = 1

for letter in player.keys():
    if player[letter] >= 5:
        result += letter

if len(result) == 0:
    print("PREDAJA")
else:
    result = ''.join(sorted(result))
    print(result)