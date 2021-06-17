# Tuples are basically an immutable list.
# Use a tuple for data that won't change.
coordinates = (30.145, 45.678)
print(coordinates[0])
print("Coordinates: " + str(coordinates[0]) + ", " + str(coordinates[1]))

# optionally, Unpack values
x, y = coordinates
print(f"Coordinates: {str(x)}, {str(y)}")

# Another way to make a tuple, or change a list to a tuple
user_data_list = ["Joe", 22, "Boston", 44.124, True]
print(f'Data type of user_data_list: {type(user_data_list)}')
tuple_data = tuple(user_data_list)
print(f'Data type of tuple_data: {type(tuple_data)}')

# unpacking elements
name, age, location, score, isMale = tuple_data
print(
    f'Unpacking elements: {name} is {age} years old, and lives in {location}.')

# Like lists, tuples can have several data types.
values = ("https://www.", "192.1.1.1", 134.578, 4, False)
for value in values:
    print(value, end='')
    print(" " + str(type(value)))

# quickly check for a value in a tuple
if 4 in values:
    print('4 is in the "values" tuple')

# access sections of a tuple - make new tuples
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[2:5]
c = a[:6]
d = a[3:]
e = a[::1]  # same as "e = a[:]""
f = a[::2]  # every second tuple
g = a[::-1]  # reverse the order of the tuple values
print(f'sections of the tuple "a": {b} {c} {d} {e} {f} {g}')

# unpack a tuple into ranged lists and/or values
i0, *i1, i9 = a
print(f'Values and lists: {i0} {i1} {i9}')

# swap variable values with a tuple
x = 'x'
y = 'y'
(x, y) = (y, x)
print(f'Swapped variables: x = {x}  y = {y}')


# return more than one value from a function using a tuple
def return_values_and_sum(x, y):
    return (x, y, x + y)
