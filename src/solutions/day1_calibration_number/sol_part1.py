from util.helper import get_numerical, open_file


def calibration_number(calibration_rel_file_path):
    file = open_file(calibration_rel_file_path)
    calibr_number = 0
    for x in file:
        numbers = get_numerical(x)
        line_number = numbers[0] * 10 + numbers[-1]
        calibr_number += line_number
    file.close()
    return calibr_number


print(calibration_number("problems/day1_calibration_number/input.txt"))
