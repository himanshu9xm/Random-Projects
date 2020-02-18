
n = int(input())
student_marks = []

for _ in range(n):
    name, m1, m2, m3 = input().split()
    student_marks.append(name)
    student_marks.append(m1)
    student_marks.append(m2)
    student_marks.append(m3)
query_input = input()
x = student_marks.index(query_input)
m1 = float(student_marks[x+1])
m2 = float(student_marks[x+2])
m3 = float(student_marks[x+3])
avg = (m1+m2+m3)/3
print(format(avg,'.2f'))
#print(student_marks)