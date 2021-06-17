# import the find_max function from the 'utils' module
#  python 3 module index: https://docs.python.org/3/py-modindex.html

from utils import find_max
import random
print('The max number is : ')
print(find_max([6, 78, -9, 45, 64, 2, 34, 1]))

print('Three instances of random.random()')
for i in range(3):
    print(random.random())

print('Three random integers from 10-20:')
for i in range(3):
    print(random.randint(10, 20))

print('Select a random element from a sequence/list:')
members = ['John', 'Larry', 'Mary', 'Sarah']
leader = random.choice(members)
print(leader)
