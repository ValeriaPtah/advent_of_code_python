import re

from util.helper import open_file, get_full_input

cube_colours_amounts = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def cube_conundrum(game_rel_file_path):
    file = open_file(game_rel_file_path)
    game_id_sum = 0
    for line in file:
        if is_game_possible(line):
            game_id = get_game_id(line)
            game_id_sum += game_id
    file.close()
    return game_id_sum


def get_game_id(game_line):
    return int(re.search(r'Game (\d+)', game_line).group(1))


def get_max_cubes_for_colour(game_line):
    cube_colour_max_amount = {}
    for colour in cube_colours_amounts:
        cube_colour_max_amount[colour] = max(map(int, re.findall(r'(\d+) ' + colour, game_line)), default=0)
    return cube_colour_max_amount


def is_game_possible(game_line):
    game_max_cube_colours_amount = get_max_cubes_for_colour(game_line)
    for colour in cube_colours_amounts:
        if cube_colours_amounts[colour] < game_max_cube_colours_amount[colour]:
            return False
    return True


print(cube_conundrum(get_full_input("day2_cube_conundrum")))
