import sys

n, m = map(int, sys.stdin.readline().split())
guide = {}
guide_reverse = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    guide[i + 1] = name
    guide_reverse[name] = i + 1

for i in range(m):
    question = sys.stdin.readline().strip()
    if question.isalpha():
        print(guide_reverse[question])
    else:
        print(guide[int(question)])