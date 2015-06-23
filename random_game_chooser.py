__author__ = 'Luke Merrett'

from analytics import playtime

if __name__ == '__main__':
    game_to_play = playtime.choose_a_random_never_played_game_to_play()
    print('You should totally play: "' + game_to_play + '"')
