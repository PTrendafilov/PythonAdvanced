students_dict={}
n=int(input())
for i in range(n):
    s=input().split()
    student=s[0]
    mark=s[1]
    if student not in students_dict:
        students_dict[student]=[]
    students_dict[student].append(float(mark))
#print(students_dict)
for student,grades in students_dict.items():
    grades_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    grades_avg=sum(grades)/len(grades)
    print(f"{student} -> {grades_formatted} (avg: {grades_avg:.2f})")
