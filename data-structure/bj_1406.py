import sys

string1 = list(sys.stdin.readline().rstrip())
string2 = []

m = int(sys.stdin.readline())

for i in range(m):
    command = (sys.stdin.readline()).split()
    if command[0] == 'L':
        if string1:
            string2.append(string1.pop())
    elif command[0] == 'D':
        if string2:
            string1.append(string2.pop())
    elif command[0] == 'B':
        if string1:
            string1.pop()
    else:
        string1.append(command[1])

string1.extend(reversed(string2))
print(''.join(string1))