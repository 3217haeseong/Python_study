#marks.py

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]>=60:
        print("%d번 학생은 합격입니다."%(number+1))
        
