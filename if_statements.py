is_male = True
is_tall = True

# If statement
if is_male:
    print("You are male.")
else:
    print("You are not male.")

# Else-If statements
if is_male or is_tall:
    print("You are male or tall or both.")
elif is_male and is_tall:
    print("You are male and tall.")
else:
    print("You are not male or not tall or both.")


def max_num(num1, num2, num3):
    if num1 >= num2 or num1 >= num3:
        return num1
    elif num2 >= num1 or num2 >= num3:
        return num2
    else:
        return num3


print("Maximum numbers:")
print(max_num(1, 2, 3))
print(max_num(1000, 2, 3))
print(max_num(1, 2.14157, 2))

print("BASIC CALCULATOR")
num1 = float(input("Enter first number: "))
operator = input("Enter the operator (+-*/): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
