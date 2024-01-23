from definitions import SOLUTION_PART1, SOLUTION_PART2
from util.helper import get_solution_file_for_day, get_full_input, get_test_input_part1, get_solution_function_for_day

DAY = "day3_gear_ratios"


def test_part1_init():
    run_test(SOLUTION_PART1, get_test_input_part1(DAY), 4361)


def test_part2_init():
    run_test(SOLUTION_PART2, get_test_input_part1(DAY), 467835)


def test_part1_final():
    run_test(SOLUTION_PART1, get_full_input(DAY), 525119)


def test_part2_final():
    run_test(SOLUTION_PART2, get_full_input(DAY), 76504829)


def run_test(solutions_file, problem_input, correct_number):
    module = get_day_src(solutions_file)
    test_function = getattr(module, get_solution_function_for_day(DAY))
    assert test_function(problem_input) == correct_number


def get_day_src(solutions_file):
    return get_solution_file_for_day(DAY, solutions_file)
