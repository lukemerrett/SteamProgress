__author__ = 'Luke Merrett'

import random
from clients.steamapi import SteamApiClient

def get_total_playtime_for_last_two_weeks():
    """
    Calculates the total time in minutes played in the last two weeks
    :return: The total playtime in minutes for the last two weeks
    """
    response = SteamApiClient().get_player_owned_games()
    return __add_numeric_key_values(response, 'playtime_2weeks')

def get_total_playtime_ever():
    """
    Calculates the total time in minutes played ever
    :return: The total playtime in minutes ever
    """
    response = SteamApiClient().get_player_owned_games()
    return __add_numeric_key_values(response, 'playtime_forever')

def get_list_of_games_never_played():
    """
    Gets a list of all the games that have never been played on this account
    :return: A list of games you should really play
    """
    response = SteamApiClient().get_player_owned_games()

    games_never_played = []

    for game in response['response']['games']:
        if 'playtime_forever' in game:
            if game['playtime_forever'] == 0:
                games_never_played.append(game['name'])

    return games_never_played

def choose_a_random_never_played_game_to_play():
    """
    Gets a single random games from the list of games never played
    that you should really play now.
    :return: A game to play that you've never played
    """
    games_never_played = get_list_of_games_never_played()

    random_int = random.randrange(games_never_played.__len__())
    return games_never_played[random_int]

def __add_numeric_key_values(response, key_to_add):
    total = 0

    for game in response['response']['games']:
        if key_to_add in game:
            total += game[key_to_add]

    return total