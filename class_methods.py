# class methods - act on the class itself.
# Typically not used on individual objects.
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def get_total_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Joey")

print(f'Total Person objects: {Person.get_total_people()}')
print(
    f'Total according to "joey": {p1.get_total_people()}')
