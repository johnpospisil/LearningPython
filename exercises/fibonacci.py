# Create the fibonacci sequence given the 'index' of the desired number:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,...
def find_fib_seq(index):
    # check if index is an integer 0 or larger
    if isinstance(index, int) == False or index < 0:
        return('Invalid user input.')

    fib_seq = [0]
    for value in range(1, index+1):
        if value == 1 or value == 2:
            fib_seq.append(1)
        elif value > 2:
            fib_seq.append(fib_seq[value-2] + fib_seq[value-1])
    return fib_seq


# test the function
print(find_fib_seq(0))
print(find_fib_seq(1))
print(find_fib_seq(5))
print(find_fib_seq(10))
print(find_fib_seq(20))
print(find_fib_seq(-5))  # invalid user input
print(find_fib_seq(0.5))  # invalid user input
print(find_fib_seq('a'))  # invalid user input
