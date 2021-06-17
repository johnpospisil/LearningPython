# Functions break up code into smaller chunks
# Code that performs a task is a good candidate for a function.

# Function without parameters
def say_hi():
    print("Hi!")


say_hi()


# Function with parameters
def say_hello(name, age):
    print("Hi, " + name + ", you are " + age + " years old.")


say_hello("Enrique", "41")

# keyword arguments - useful when you want to see how the data will be used from the function call
say_hello(age="33", name="Jose")

# Functions can return data


def cubed(num):
    return num*num*num


print(cubed(2))
