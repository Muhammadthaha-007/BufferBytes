

def gradingStudents(grades):
    if max(grades) <= 100:
        for grade in grades:
            if grade < 38:
                print(grade)
            else:
                n = 1
                while n < 5:
                    if (grade + n) - grade >= 3 and (grade + n) % 5 == 0:
                        print(grade)
                    elif (grade + n) - grade < 3 and (grade + n) % 5 == 0:
                        print(grade+n)
                    n += 1

print(gradingStudents([73,67,38,33]))