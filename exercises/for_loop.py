# find the total of the prices
prices = [10, 20, 30, 4, 3, 67, 87, 44, 34, 2, 12, 3, 4, 55, 46.36]

total = 0
for price in prices:
    total += price
print(f'Total Price: ${total}')


# print rows of stars based on a list of integers
numbers = [5, 2, 3, 4, 6]

for number in numbers:
    print(number * '*')


# find the largest number in a list
def highest_price(prices):
    highest_number = 0
    for price in prices:
        if price > highest_number:
            highest_number = price

    return highest_number


print(highest_price(prices))

# remove duplicates from a list
values = [4, 5, 3, 3, 8, 3, 4, 5, 7]
unique_values = []

print(f'Original List: {values}')
for value in values:
    # count the occurences of a value.
    if value not in unique_values:  # If count > 1, remove additional occurrences of 'value'
        unique_values.append(value)
print(f'Duplicates Removed: {unique_values}')
