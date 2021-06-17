# class attributes - attributes that are specific to the class,
# not to an instance of that class.

class Person:
    # a class attribute. It is specific to the class, not an instance of the class.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person("Joey")

print(f'number of people according to a Person object: {p1.number_of_people}')

# class attributes can also be accessed from the Person class directly
print(
    f'number_of_people according to the Person class: {Person.number_of_people}')

Person.number_of_people = 2
print(
    f'updated number_of_people according to the Person class: {Person.number_of_people}')
print(
    f'updated number of people according to a Person object: {p1.number_of_people}')
