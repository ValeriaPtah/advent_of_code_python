import os
import re
from importlib import import_module

from definitions import ROOT_DIR, SOLUTIONS_MODULE


# remember to close later
def open_file(rel_file_path):
    return open(get_project_file_path(rel_file_path))


def get_project_file_path(rel_file_path):
    return os.path.join(ROOT_DIR, rel_file_path)


def get_numerical(line):
    return list(map(int, filter(lambda i: i.isdigit(), line)))


def get_solution_file_for_day(day_folder, solution_file):
    return import_module(SOLUTIONS_MODULE + '.' + day_folder + '.' + solution_file)


def get_solution_function_for_day(day_folder_name):
    return re.sub(r'day(\d+)_', '', day_folder_name)


def get_full_input(day):
    return "problems/{day}/input.txt".format(day=day)


def get_test_input_part1(day):
    return "problems/{day}/test_input1.txt".format(day=day)


def get_test_input_part2(day):
    if os.path.isfile("problems/{day}/test_input2.txt".format(day=day)):
        return "problems/{day}/test_input2.txt".format(day=day)
    else:
        return get_test_input_part1(day)
