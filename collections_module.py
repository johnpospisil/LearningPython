# Collections Module: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

print('\nCOUNTERS')
# Counter - count the occurrences of a character in a string
my_string = 'abadacdcbdcadcbdcdadbc'
my_counter = Counter(my_string)
print(f'String: {my_string}\n{my_counter}\n')

# access data in a Counter like a dictionary
print('Access data in a counter')
print(f'Keys: {my_counter.keys()}\nValues: {my_counter.values()}\nItems: {my_counter.items()}\n')

# .most_common(int) elements - returns a list of tuples
print(f'Most common element in my_string is {my_counter.most_common(1)}')
print(
    f'1st and 2nd most common elements in my_string are {my_counter.most_common(2)}')
print(
    f'1st, 2nd and 3rd most common elements in my_string are {my_counter.most_common(3)}\n')

# access specific counter elements in a tuple
print(
    f'Most common element: {my_counter.most_common(1)[0][0]}\nElement count: {my_counter.most_common(1)[0][1]}\n')

# convert Counter elements to a list
print('Convert elements to a list')
print(list(my_counter.elements()))

# namedtuple - an easy-to-create and lighweight object type, similar to a struct
print('\nNAMEDTUPLE')
# make a Point class and assign some values
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(f'Point Object: {pt} \nPoint Values: {pt.x}, {pt.y}')

# OrderedDict - allows for ordered dictionaries.
# This is a standard feature in dictionaries after Python 3.7,
# so ordered dictionaries are often found in older code.
print('\nORDEREDDICT')
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict - a dictionary that allows a default value if the value has not yet been set
# below, an integer with a default value of '0' is returned when a missing key is called
print('DEFAULTDICT')
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(f"Default Dictionary: {d}")
print(f"a -> {d['a']}\nb -> {d['b']}\nc -> {d['c']}")

# deque - a double-ended queue.
# Can be used to efficiently add/remove elements from both ends of a list.
print('\nDEQUE')
d = deque()

# add elements
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)

# add elements to the left side
d.appendleft(0)
print(d)

# add multiple elements
d.extend([5, 6, 7])
print(d)

# add multiple elements to the left
d.extendleft([-1, -2, -3])
print(d)

# remove last element
d.pop()
print(d)

# remove first element
d.popleft()
print(d)

# rotate the list
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-3)
print(d)

# clear elements
d.clear()
print(d)
