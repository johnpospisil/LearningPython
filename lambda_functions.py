from functools import reduce
# lambda functions are one-line ananymous functions without a function name.
# Use them:
# 1. when you want to use a function once
# 2. when you have a simple function
# 3. as an input to a higher order function

# they are structered as follows:
# lambda arguments: expression
print('\nLAMBDA FUNCTIONS')
# a lambda function
def add10(x): return x + 10


print(f'lambda function add10(5) -> {add10(5)}')


# standard function - note the extra line
def add_10(x):
    return x + 10


# lambda function with multiple inputs
def mult(x, y): x*y


print(f'multi-input lambda function mult(7,6) -> {mult(7, 6)}\n')

# sorted - reorders lists with a lambda function
print('SORTED')
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D)
points2D_sorted_y = sorted(points2D, key=lambda x: x[1])
points2D_sorted_sum = sorted(points2D, key=lambda x: x[0] + x[1])

print(f'2D points: {points2D}')
print(f'2D points, sorted: {points2D_sorted}')
print(f'2D points, sorted by \'y\' values: {points2D_sorted_y}')
print(
    f'2D points, sorted by sum of \'x\' and \'y\' values: {points2D_sorted_sum}')

# map functions - take a list, copy it, perform an action on each element, and return the new list
#map(func, seq)
print('\nMAP FUNCTION')
a = [1, 2, 3, 4]
b = map(lambda x: x*2, a)
print(f'map function output: {list(b)}')

# lambda functions are popular, however,
# it is easier to achieve the above as follows:
c = [x*2 for x in a]
print(f'modern output: {list(c)}')


# filter function
# filter(func, seq)
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e = filter(lambda x: x % 2 == 1, d)
print(f'filter function, return odd numbers only: {list(e)}')

# modern notation for filtering
f = [x for x in d if x % 2 == 0]
print(f'modern filter function, evens only: {list(f)}')


# reduce function - repeatedly applies the function to telements, returning a single value
# reduce(func, seq)
g = [1, 2, 3, 4, 5, 6]
product_g = reduce(lambda x, y: x*y, g)
print(f'reduce function, return the product of a list: {product_g}')
