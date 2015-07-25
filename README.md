# SteamProgress

Tracks progress in Steam games and helps choose games to play.

Includes a set of utilities as outlined below:

## Random Game Chooser

Can choose a random game from your Steam collection that you've never played.

    usage: python random_game_chooser.py [-h] [-np] [-i]

    optional arguments:
      -h, --help           show this help message and exit
      -np, --never-played  Only returns games you've never played
      -i, --installed      Only returns games that are currently installed

## List All Games

Lists all games within your account, whether they are installed and how long they've been played for.

    usage: python list_all_games.py

## Store Playtime

Stores your currently playtime for the last 2 weeks per game in a local SQLite database.

    usage: python store_playtime.py

## Graph Playtime

Outputs an SVG graph in your browser showing rolling playtime captured each day using the above script

    usage: python graph_playtime.py