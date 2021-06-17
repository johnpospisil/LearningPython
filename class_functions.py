from Student import Student

student1 = Student("Jim", "Business", 3.6, False)
student2 = Student("Tammy", "Mathematics", 2.0, True)

print("HONOR ROLL STATUS")
print(student1.name + ": " + str(student1.on_honor_roll()))
print(student2.name + ": " + str(student2.on_honor_roll()))
