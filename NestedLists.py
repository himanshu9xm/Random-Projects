N = int(input())
marks = []
SMAX = 0
for i in range(N):
    name = input()
    grade = input()
    marks.append([float(grade), name])

marks.sort()
# print(marks)

MAX = marks[-1][0]

for i in range(0, N):
    if marks[N - i - 1][0] < MAX:
        SMAX = marks[i][0]
        # print(SMAX)
        break

for i in range(N):
    if marks[i][0] == SMAX:
        print(marks[i][1])
    elif marks[i][0] > SMAX:
        break
