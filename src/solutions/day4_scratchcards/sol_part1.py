import re

from util.helper import open_file, get_full_input


def scratchcards(game_rel_file_path):
    file = open_file(game_rel_file_path)
    pile_worth = 0
    for line in file:
        amount_of_matches_per_card = get_amount_of_matches(line)
        pile_worth += get_card_power(amount_of_matches_per_card)
    file.close()
    return pile_worth


def get_amount_of_matches(card):
    winning_numbers = get_winning_numbers(card)
    given_numbers = get_given_numbers(card)
    return len(list(set(given_numbers).intersection(winning_numbers)))


def get_winning_numbers(card):
    pattern = r':\s*([\d\s]+)\|'
    return [int(num) for num in re.search(pattern, card).group(1).split()]


def get_given_numbers(card):
    pattern = r'\|\s*([\d\s]+)$'
    return [int(num) for num in re.findall(r'\d+', re.search(pattern, card).group(1))]


def get_card_power(amount_of_matches):
    if amount_of_matches > 0:
        return 2 ** (amount_of_matches - 1)
    return 0


print(scratchcards(get_full_input("day4_scratchcards")))
