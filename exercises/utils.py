def find_max(number_list):
    largest_number = 0
    for number in number_list:
        if number > largest_number:
            largest_number = number
    return largest_number
