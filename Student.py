# Classes are instructions to create atype of object
# Objects are an instance of a Class

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# A class function
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
