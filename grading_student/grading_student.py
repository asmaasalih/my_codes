def gradingStudents(grades):
    #
    # Write your code here.
    #
    new_grades = []
    for grade in grades:
        rounded_grade = (int(grade/5)+1)*5
        if grade < 38:
            new_grades.append(grade)
        else:
            if rounded_grade - grade < 3:
                new_grades.append(rounded_grade)
            else:
                new_grades.append(grade)
    return new_grades            
                