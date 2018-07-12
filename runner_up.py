    n = int(input())
  2 student_marks = {}
  3 for _ in range(n):
  4         name, *line = input().split()
  5         score = list(map(float, line))
  6         student_marks[name] =  score
  7 print(student_marks)
  8 query_name = input()
  9 lis = student_marks[query_name]
 10 second_max = max(n for n in lis if n != max(lis))
 11 print("%.2f" % second_max)

