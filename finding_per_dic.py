n = int(input())
student_marks = {}
for _ in range(n):
	name, *line = input().split()
	score = list(map(float, line))
	student_marks[name] =  score
print(student_marks)
query_name = input()
lis = student_marks[query_name]
x = len(lis)
avg = sum(lis)/x
print("%.2f" % avg)
