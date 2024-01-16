from util.helper import remove_non_numerical, open_file


def count_calibration(calibration_rel_file_path):
    file = open_file(calibration_rel_file_path)
    calibration_number = 0
    for x in file:
        numbers = remove_non_numerical(x)
        line_number = int(numbers[0]) * 10 + int(numbers[-1])
        calibration_number += line_number
    file.close()
    return calibration_number


print(count_calibration("problems/day1_calibration_number/input.txt"))
