import os
from importlib import import_module

from definitions import ROOT_DIR, SOLUTIONS_MODULE


# remember to close later
def open_file(rel_file_path):
    return open(get_project_file_path(rel_file_path))


def get_project_file_path(rel_file_path):
    return os.path.join(ROOT_DIR, rel_file_path)


def remove_non_numerical(line):
    return list(filter(lambda i: i.isdigit(), line))


def get_solutions_file_for_day(day_folder, solution_file):
    return import_module(SOLUTIONS_MODULE + '.' + day_folder + '.' + solution_file)


def get_full_input(day):
    return "problems/{day}/input.txt".format(day=day)


def get_test_input_part1(day):
    return "problems/{day}/test_input1.txt".format(day=day)


def get_test_input_part2(day):
    return "problems/{day}/test_input2.txt".format(day=day)
