class Student:

    def __init__(self, name):
       self.average = None
       self.name = name
       self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        self.average = sum(self.grades) / len(self.grades)
        return self.average

    def __str__(self):
        return f"{self.name}, {self.average}"

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        x = 0
        top = []
        for student in self.students:
            if x < student[1]:
                x = student[1]
        for student in self.students:
            if student[1] == x: top.append(student)
        return top

    def get_failed_students(self):
        failure = []
        for student in self.students:
            if student[1] < 51: failure.append(student)
        return failure

p1 = Student("John")
p1.add_grade(10)
p1.add_grade(20)
p1.add_grade(30)

print(p1.get_average_grade())
print(p1)
