# for-loop for each line of the input file
# remove the a-z, none-numerical (regex?)
# pick first (decimals) and last (ordinary) digits
# add to the sum

import os

from definitions import ROOT_DIR


def count_calibration(calibration_rel_file_path):
    calibration_file_path = os.path.join(ROOT_DIR, calibration_rel_file_path)
    calibration_number = 0
    file = open(calibration_file_path)
    for x in file:
        numbers = remove_non_numerical(x)
        line_number = int(numbers[0]) * 10 + int(numbers[-1])
        calibration_number += line_number
    file.close()
    return calibration_number


def remove_non_numerical(line):
    return list(filter(lambda i: i.isdigit(), line))


print(count_calibration("problems/day1/inp1.txt"))
