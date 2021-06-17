#  Used to loop through a collections of items like chars, lists, onjects, etc.

# Loop through characters
for char in "Forger":
    print(char, end=' ')
print("")

# Loop through lists
friends = ["Karen", "Koko", "Jimmy", "Albert", "Zoltan"]

for friend in friends:
    print(friend, end=' ')
print("")

# Loop with an index
for index in range(10):
    print(index, end=' ')
print("")

for index in range(3, 10):
    print(index, end=' ')
print("")

for index in range(3, 10, 2):
    print(index, end=' ')
print("")


# Excercise: make a power function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = base_num * result
    return result


print(raise_to_power(3, 4))

# Nested for loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]
for row in number_grid:
    for col in row:
        print(col, end=' ')
    print("")
