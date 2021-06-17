# READ the file
employee_file = open("employees.txt", "r")

print(employee_file.read())
# print(employee_file.readline())
# for employee in employee_file.readlines():
#     print(employee)

employee_file.close()
