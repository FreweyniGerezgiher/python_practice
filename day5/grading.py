student_score = {"harry": 81,"ron": 78, "hana": 99,"dan": 74, "nati":62,}
student_grade = {}
for key in student_score:
    if student_score[key] >= 91:
        student_grade[key] = "outstanding"
    elif student_score[key] >= 81:
        student_grade[key] = "Exceeds Expectation"
    elif student_score[key] >= 71:
        student_grade[key] = "Acceptable"
    elif student_score[key] <=70:
        student_grade[key] = "fail"
print(student_grade)
