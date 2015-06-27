# SteamProgress

Tracks progress in Steam games and helps choose games to play.

Includes a set of utilities as outlined below:

## Random Game Chooser

Can choose a random game from your Steam collection that you've never played.

    usage: random_game_chooser.py [-h] [-np] [-i]

    optional arguments:
      -h, --help           show this help message and exit
      -np, --never-played  Only returns games you've never played
      -i, --installed      Only returns games that are currently installed

## List All Games

Lists all games within your account and whether they are installed

    usage: list_all_games.py
