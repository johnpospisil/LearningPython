# Time operations. Two for loops are timed below.
from timeit import default_timer as timer

start = timer()
sum = 0
for i in range(10):
    sum += 1
end = timer()
print(f'\n10 loops: {end-start}s')

start = timer()
sum = 0
for i in range(1000000):
    sum += 1
end = timer()
print(f'1,0000,000 loops: {end-start}s')

start = timer()
sum = 0
for i in range(1000000):
    sum = sum + 1
end = timer()
print(f'1,0000,000 loops: {end-start}s')
