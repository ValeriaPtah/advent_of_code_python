import math
import re

from util.helper import open_file, get_full_input

cube_colours = {"red", "green", "blue"}


def cube_conundrum(game_rel_file_path):
    file = open_file(game_rel_file_path)
    total_power = 0
    for line in file:
        total_power += get_game_set_power(line)
    file.close()
    return total_power


def get_min_required_cube_set(game_line):
    cube_colour_max_amount = {}
    for colour in cube_colours:
        cube_colour_max_amount[colour] = max(map(int, re.findall(r'(\d+) ' + colour, game_line)), default=0)
    return cube_colour_max_amount


def get_game_set_power(game_line):
    min_required_cube_set = get_min_required_cube_set(game_line)
    return math.prod(min_required_cube_set.values())


print(cube_conundrum(get_full_input("day2_cube_conundrum")))
