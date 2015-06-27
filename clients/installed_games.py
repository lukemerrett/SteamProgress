import os
import settings

__installed_games = os.listdir(settings.steam_user_folder)

def is_game_in_installed_games_list(game):
    return str(game['appid']) in __installed_games
