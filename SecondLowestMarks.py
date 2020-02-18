N = int(input())
#student_marks = list(input().split() for _ in range(N))
#student_marks.sort(key = value)
student_marks = []

for i in range(N):
	name, score = input().split()
	a = []
	a.append(name)
	a.append(score)
	student_marks.append(a)
#print(student_marks)
def takeSecond(elem):
    return elem[1]

student_marks.sort(key = takeSecond)
print(student_marks)