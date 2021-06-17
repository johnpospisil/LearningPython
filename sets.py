# sets - like an unordered, mutable list. No duplicate elements allowed.

# make a set
set1 = {1, 2, 3, 1, 2}
print(set1)

set2 = set([4, 5, 6])
print(set2)

# make a set of unique characters from a string
set3 = set('hello')
print(f'A set containing the word "hello": {set3}')

# add an element to a set with .add()
set1.add(4)
print(set1)

# remove an element with .remove() - can raise errors if no matching element
set1.remove(1)
print(set1)

# remove an element with .discard() - won't raise errors if no matching element
set1.discard(2)
set1.discard(2345)
print(set1)

# clear a set with .clear()
set1.clear()
print(set1)

# .pop() remove and return an arbitrary element from a set;
popped_element = set2.pop()
print(f'\nPopped Element: {popped_element}')

# loop over a set
print('Items in set2:')
for item in set2:
    print(item)

# check for a value in an element in a set
if 5 in set2:
    print('"5" is in set2.')


# Union and Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(
    f'\nUNION and INTERSECTION\nodds: {odds}\nevens: {evens}\nprimes: {primes}')

# unions of sets
u = odds.union(primes)
print(f'Union of odds and primes: {u}')

# intersections of sets
i = odds.intersection(primes)
print(f'Intersection of odds and primes: {i}')

# difference between sets
diff1 = odds.difference(primes)
diff2 = primes.difference(odds)
print(f'Difference between odds and primes: {diff1}')
print(f'Difference between primes and odds: {diff2}')

# symmetric difference between sets
sym_diff = odds.symmetric_difference(primes)
print(f'Symmetric Difference between odds and primes: {sym_diff}')

# DESTRUCTIVE FUNCTIONS BELOW
print('\nDESTRUCTION FUNCTIONS BELOW')
# merge between sets
odds.update(primes)
print(f'Merge between odds and primes with .update(): {odds}')

# intersection update
evens.intersection_update(primes)
print(
    f'Intersection Update between evens and primes with .intersection_update(): {evens}')

# difference update
{1, 3, 5, 7, 9}.difference_update(primes)
print(
    f'Difference Update between odds and primes with .difference_update(): {evens}')

# symmetric difference update
odds2 = {1, 3, 5, 7, 9}
primes2 = {2, 3, 5, 7}
odds2.symmetric_difference_update(primes2)
print(
    f'Symmetric Difference Update between odds and primes with .difference_update(): {odds2}')

# check if one set is subset/superset of a second set
set_a = {1, 2, 3, 4, 5, 6}
set_b = {1, 2, 3}
print(f'\nset_a: {set_a}\nset_b: {set_b}')
print(f'Is set_b a subset of set_a? {set_b.issubset(set_a)}')
print(f'Is set_a a superset of set_b? {set_a.issuperset(set_b)}')
set_c = {4, 5, 6}

# .isdisjoint() - returns TRUE if no elements are the same between sets
print(f'set_c: {set_c}\nIs set_b disjoint from set_c? {set_b.isdisjoint(set_c)}')

# copy a set - two ways
set_d = set_c.copy()
set_e = set(set_c)
print(f'Source Set: {set_c} Copied Set1: {set_d} Copied Set2: {set_e}')

# FROZEN SET - an immutable set that cannot be changed after creation
frozn_set = frozenset([1, 2, 3, 4])
print(f'Frozen sets are immutable: {frozn_set}')
