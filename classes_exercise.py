# OOP in Python
# create student and course classes
# find the average student grade for any course

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # a list of all students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):  # return average grade of all students in a course
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)


s1 = Student("Rory", 18, 77)
s2 = Student("Edgar", 19, 82)
s3 = Student("Susan", 20, 92)

course = Course('Physics 131', 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(f'Average student grade for Physics 131: {course.get_average_grade()}%')
