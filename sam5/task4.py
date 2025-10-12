def fix_grades(grades):
    fixed_grades = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            fixed_grades.append(4)
        else:
            fixed_grades.append(grade)
    return fixed_grades

grades_list_1 = [2, 3, 4, 5, 3, 4, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 5, 5, 5, 3, 3, 3, 5, 4, 4]

fixed_1 = fix_grades(grades_list_1)
fixed_2 = fix_grades(grades_list_2)
fixed_3 = fix_grades(grades_list_3)

print(f"Исходные оценки 1: {grades_list_1}")
print(f"Исправленные оценки 1: {fixed_1}")
print(f"Исходные оценки 2: {grades_list_2}")
print(f"Исправленные оценки 2: {fixed_2}")
print(f"Исходные оценки 3: {grades_list_3}")
print(f"Исправленные оценки 3: {fixed_3}")