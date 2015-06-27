__author__ = 'Luke Merrett'

import os
import random
import settings
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

def choose_a_random_game_to_play(choose_never_played, choose_installed):
    """
    Gets a single random games from the list of games
    that you should really play now.
    :return: A game to play
    """
    games = SteamApiClient().get_player_owned_games()['response']['games']

    if choose_never_played:
        games_never_played = []
        for game in games:
            if 'playtime_forever' in game:
                if game['playtime_forever'] == 0:
                    games_never_played.append(game)
        games = games_never_played

    if choose_installed:
        installed_games = []
        installed_game_folders = os.listdir(settings.steam_user_folder)
        for game in games:
            appid = str(game['appid'])
            if appid in installed_game_folders:
                installed_games.append(game)
        games = installed_games

    if games.__len__() == 0:
        return 'Could not find any games you can play!'

    random_int = random.randrange(games.__len__())
    return games[random_int]['name']

def __add_numeric_key_values(response, key_to_add):
    total = 0

    for game in response['response']['games']:
        if key_to_add in game:
            total += game[key_to_add]

    return total
