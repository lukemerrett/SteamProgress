from clients import installed_games, steamapi

if __name__ == '__main__':
    api = steamapi.SteamApiClient()
    games = api.get_player_owned_games()
    for game in games:
        game['installed'] = installed_games.is_game_in_installed_games_list(game)

    for game in sorted(games, key=lambda game: game['name']):
        installed = 'Yes' if game['installed'] else 'No'
        print (game['name'])
        print('    Installed: ' + installed)
        print('    Playtime in Minutes: ' + str(game['playtime_forever']))
        print('')
