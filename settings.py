__author__ = 'Luke Merrett'

steam_webapi_key = 'Get your key here http://steamcommunity.com/dev'
registered_domain = 'The domain used to register above'
steam_user_id = 'Enter your user id here'
steam_user_folder = 'Enter your user folder here, eg C:\\Program Files (x86)\\Steam\\userdata\\22222222'

# Maybe you brought some games you'll never play (how could you)
# Add them in your local settings to exclude from the random game chooser
ignored_games = ['Game name to ignore']

# How about games you've already completed?
# These should go here to exclude them from the random game chooser
completed_games = ['Completed game name']

# API settings
# Full template: http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>.
steam_api_url = 'http://api.steampowered.com/'
response_format = 'json'

# Database settings
sqlite_database_name = 'SteamProgress.db'

# Charting settings
target_chart_export_filename = 'stored_playtime.svg'

# Override with your local settings, stops them being committed to GitHub
try:
    from local_settings import *
except ImportError:
    pass

# Do not modify, this just simplifies the code later on.
excluded_games = []
excluded_games.extend(ignored_games)
excluded_games.extend(completed_games)
