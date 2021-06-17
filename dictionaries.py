# Dictionaries are an unordered mutable list of key/value pairs, much like an actual dictionary.

# Two ways to amke a dictionary:
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

monthConversions2 = dict(
    Jan="January",
    Feb="February",
    Mar="March",
)

# Enter a key, get the value
print(monthConversions["Jan"])
print(monthConversions["Mar"])

# Enter an invalid key, get a default value
print(monthConversions.get("wrong_key", "Not a valid key"))

# add a key-value pair
monthConversions["Apr"] = "April"
print(f'Add a key-value pair: {monthConversions}')

# delete a key-value pair - 3 ways:
del monthConversions["Apr"]
print(f'Delete "Apr": {monthConversions}')
monthConversions.pop("Mar")
print(f'Delete "Mar": {monthConversions}')
monthConversions.popitem()
print(f'Delete the most recently added key-value pair: {monthConversions}')

# check for a key in a dictionary
if "Mar" in monthConversions2:
    print(
        f'The value for "Mar" is in the dictionary and is: {monthConversions2["Mar"]}')

# loop through a dictionary
print('\nKEY - basic for-in loop')
for key in monthConversions2:
    print(key)

print('KEY - loop using the ".keys()" function ')
for key in monthConversions2.keys():
    print(key)

print('VALUE - loop using the ".values()" function ')
for value in monthConversions2.values():
    print(value)

print('\nKEY : VALUE - loop using the ".items()" function ')
for key, value in monthConversions2.items():
    print(f'{key} : {value}')

# copy a dictionary with .copy() function
monthConversions3 = monthConversions2.copy()
print(f'\nCopy a dictionary with the .copy() function: {monthConversions3}')

# merge dictionaries with .update()
dictn1 = dict(name="Joseph", age=34, email="joe@mail.com")
dictn2 = dict(name="Mary", age=27, location="Boston")
print(
    f'\nMerge Dictionaries with .update()\nDictionary 1: {dictn1}\nDictionary 2: {dictn2}')

dictn1.update(dictn2)
print(f'Dictionary 1 after Merge: {dictn1}')

# strings, numbers, and TUPLES can be used as keys in dictionaries
dictionary = dict()
my_tuple = (106, 'owiue')
dictionary = {my_tuple: 'https://www.'}
print(f'\nKeys can be tuples. key-value pair with a TUPLE key: {dictionary}')


# exercise - change number to text
digits_mapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}
user_number = '9876543210'
print(f'\nChange Numbers to text: {user_number}')
result = ''
for digit in user_number:
    result += f'{digits_mapping[digit]} '

print(result)
