n = int(input())
student = []

for i in range(n):
    student.append(input().split())
    student[i][1] = int(student[i][1])
    student[i][2] = int(student[i][2])
    student[i][3] = int(student[i][3])

for i in range(n):
    student = sorted(student, key=lambda x : (x[3], x[2], x[1]))
    
print("{}\n{}".format(student[n - 1][0], student[0][0]))