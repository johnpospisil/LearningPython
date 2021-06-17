# Classes are instructions to create atype of object
# Objects are an instance of a Class

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Tammy", "Mathematics", 2.0, True)

print(student1.name)
print(student1.major)
print(student2.name)
print(student2.gpa)

student1.name = "Jamison"
print(student1.name)
