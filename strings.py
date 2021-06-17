# STRINGS - ordered and immutable
# Literals
print("New\nLine")
print("\"This is a quote.\" - Sample Person")
print("")

# Concatenation
phrase = "This is a string."
print(phrase)
print(phrase + " This is a concatenated string.")
print("")

# Multi-Line String
my_string = """Multi-
Line
String\n"""
print(my_string)

# Upper/lower Case Output
print("Output string to lower case: " + phrase.lower())
print("Output string to Upper case: " + phrase.upper())
print("The original string is unaffected: " + phrase)
print("")

# Check for Upper/lower Case
print("Is the original string Uppercase? " + str(phrase.isupper()))
print("Is the original string lowercase? " + str(phrase.islower()))
print("")

# Finding length of a String
print("Length of the string: " + str(len(phrase)) + " characters.")
print("")

# Accessing Characters in a String
print("The first character of the string is: \"" + phrase[0] + "\".")
print("The last character of the string is: \"" + phrase[-1] + "\".")
print("The 2nd thru 8th chars are: \"" + phrase[1:8] + "\".")

print("")

# Find the first index for a given character/string.
print("The index for the letter \"T\" is: " + str(phrase.index("T")) + ".")
print("The index for the letter \"s\" is: " + str(phrase.index("s")) + ".")
print("")

# Replace text in a String using .replace()
print("Replace a word in a string: " + phrase.replace("string", "sentence"))
print("The original string is unaffected: " + phrase)
print("")

# find the first index of a char/sub-string in a string
if "z" in phrase:
    print(f"z IS in the phrase: {phrase}")
else:
    print(f"z is NOT in the phrase: {phrase}")

# find a char/sub-string in a string with .find()
print(f'What is the index where "is a" starts? {phrase.find("is a")}')


# count occurrences of a char/sub-string with .count()
print(f'"s" occures {phrase.count("s")} times in the phrase: {phrase}\n')

# .endswith() and .startswith()
print(f'Does "{phrase}" start with "This"? {phrase.startswith("This")}')
print(f'Does "{phrase}" end with "string."? {phrase.endswith("string.")}\n')

# remove leading/tailing white spaces with .strip()
spaced_string = '   Leading/Tailing spaces will be removed from this string   '
spaced_string = spaced_string.strip()
print(spaced_string)

# change a string into a list of words using .split()
word_list = phrase.split()
print(f'\nList of words from a string: {word_list}')

# split words with commas, or other separators
groceries = "eggs, bacon, bread, salad"
groceries_list = groceries.split(', ')
print(f'String: {groceries}  List: {groceries_list}')

# join a list of words to make a string
new_string = ", ".join(groceries_list)
print(f'Change a list {groceries_list} to a string: {new_string}')

# formatting strings %, .format(), f-Strings
