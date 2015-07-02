__author__ = 'Luke Merrett'

import argparse
from analytics import playtime

def get_cmd_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-np', '--never-played',
        dest='never_played',
        action='store_true',
        help='Only returns games you\'ve never played'
    )

    parser.add_argument(
        '-i', '--installed',
        dest='installed',
        action='store_true',
        help='Only returns games that are currently installed'
    )

    return parser.parse_args()

if __name__ == '__main__':
    args = get_cmd_arguments()

    game_found, game_to_play = playtime.choose_a_random_game_to_play(
        args.never_played,
        args.installed
    )

    if not game_found:
        print('Couldn\'t find a game to play!')
    else:
        print('You should totally play: "' + game_to_play + '"')
    input()
