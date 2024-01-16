import re

from util.helper import open_file

str_to_int_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def count_calibration(calibration_rel_file_path):
    file = open_file(calibration_rel_file_path)
    calibration_number = 0
    for line in file:
        abc_line = replace_int_with_str(line)
        line_number = get_line_number(abc_line)
        calibration_number += line_number
    file.close()
    return calibration_number


def replace_int_with_str(line):
    line_with_str_numbers = line
    for number in str_to_int_dict:
        line_with_str_numbers = line_with_str_numbers.replace(str_to_int_dict.get(number), number)
    return line_with_str_numbers


def get_line_number(line):
    numbers_substrings = {}
    for number in str_to_int_dict:
        all_indices = re.finditer(number, line)
        for match in all_indices:
            # collect all indices of a str number in a line
            numbers_substrings[match.regs[0][0]] = match.group()
    first_number = numbers_substrings[min(numbers_substrings.keys())]
    last_number = numbers_substrings[max(numbers_substrings.keys())]
    return int(str_to_int_dict.get(first_number)) * 10 + int(str_to_int_dict.get(last_number))


print(count_calibration("problems/day1_calibration_number/input.txt"))
