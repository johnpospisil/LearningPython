# Itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product - find the product of arrays of numbers (aka lists)
print('PRODUCT')
a = [1, 2]
b = [3, 4]
prod = product(a, b)
prod2 = product(a, b, repeat=2)
# print(list(prod))
# print(list(prod2))
print(f'a = {a}\nb = {b}\na X b = {list(prod)}\na X b twice = {list(prod2)}')

# permutations - creates all possible permutations of a list
print('\nPERMUTATIONS')
c = [1, 2, 3]
perm = permutations(c)
perm2 = permutations(c, 2)
print(f'Permutations of {c}:')
print(list(perm))
print(f'Permutations of {c} with length = 2:')
print(list(perm2))

# combinations - create all possible combinations of elements at a given length, n
print('\nCOMBINATIONS')
d = [1, 2, 3, 4]
print(f'Combinations of {d} with length = 2:')
comb = combinations(d, 2)
print(list(comb))
print(f'Combinations of {d} with length = 3:')
comb2 = combinations(d, 3)
print(list(comb2))

# combinations with replacement - allows values to appear more than once in a combination
print(f'Combinations with replacement of {d} with length = 2:')
comb3 = combinations_with_replacement(d, 2)
print(list(comb3))
print(f'Combinations with replacement of {d} with length = 3:')
comb4 = combinations_with_replacement(d, 3)
print(list(comb4))

# accumulate - makes an iterator that returns accumulated sums of a list
print('\nACCUMULATE')
e = [1, 2, 3, 4]
acc = accumulate(e)
print(f'list = {e}')
print(f'accumulated list = {list(acc)}')

# accumulated lists can also mutiply, or perform other mathematical operations on cells
acc2 = accumulate(e, func=operator.mul)
print(f'multiplied accumulated list = {list(acc2)}')

# use accumulate to find the max value in a list,
# and retain it's value until a larger value is found
f = [1, 5, 2, 3, 6, 4, 2, 1, 7, 5]
acc3 = accumulate(f, func=max)
print(f'list = {f}')
print(f'max value in the list = {list(acc3)}')

# groupby - makes an iterator that returns groups of keys based on a pass/fail test


def smaller_than_2_test(x):
    return x < 2


print('\nGROUPBY')
g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
group_obj = groupby(g, key=smaller_than_2_test)
for key, value in group_obj:
    print(key, list(value))
# print(group_obj)

# infinite iterators (count, cycle, repeat)
print('\nINFINITE ITERATORS - count, cycle, repeat')

# count - an infinite counter
print('Count - an infinite counter')
for i in count(10):
    print(i, end=' ')
    if i == 30:
        print('\ndone: i = 30')
        break

# cycle - cycle through the values of a list infinitely
print('\nCycle - cycle endlessly through a list')
h = [1, 2, 3, 4, 5]
count = 0
for i in cycle(h):
    print(i, end=' ')
    count += 1
    if count > 20:
        print('\ndone: count is greater than 20')
        break

# repeat - repeat a number or string infinitely
print('\nRepeat - repeat a number or string endlessly')
for i in repeat("hi", 5):
    print(i, end=' ')
print("'hi' has repeated 5 times")
