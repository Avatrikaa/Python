students = [("Alice", 85), ("Bob", 78), ("Charlie", 92),
            ("David", 85), ("Eve", 78), ("Frank", 85),
            ("Mark", 50), ("George", 21)]

def unique_grades(students):
    x = set()
    check = set()
    for student in students:
        num = student[1]
        if num in check :
            if num in x:
                x.remove(num)
        else :
            x.add(num)
            check.add(num)
    return x

def top_performers(students):
    x = 0
    top = []
    for student in students:
        if x < student[1]:
            x = student[1]
    for student in students:
        if student[1] == x: top.append(student)
    return top

def failures(students):
    failure =[]
    for student in students:
        if student[1] < 51: failure.append(student)
    return failure

print(unique_grades(students))
print(top_performers(students))
print(failures(students))

