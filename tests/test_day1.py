from definitions import SOLUTION_PART1, SOLUTION_PART2
from util.helper import get_solutions_file_for_day, get_full_input, get_test_input_part1, get_test_input_part2

DAY = "day1_calibration_number"
SOLUTION_FUNCTION = "count_calibration"


def test_part1_init():
    run_test(SOLUTION_PART1, get_test_input_part1(DAY), 142)


def test_part2_init():
    run_test(SOLUTION_PART2, get_test_input_part2(DAY), 281)


def test_part1_final():
    run_test(SOLUTION_PART1, get_full_input(DAY), 55386)


def test_part2_final():
    run_test(SOLUTION_PART2, get_full_input(DAY), 54824)


def run_test(solutions_file, problem_input, correct_number):
    module = get_day_src(solutions_file)
    test_method = getattr(module, SOLUTION_FUNCTION)
    assert test_method(problem_input) == correct_number


def get_day_src(solutions_file):
    return get_solutions_file_for_day(DAY, solutions_file)
