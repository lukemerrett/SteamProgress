__author__ = 'Luke Merrett'

steam_webapi_key = 'Get your key here http://steamcommunity.com/dev'
registered_domain = 'The domain used to register above'
steam_user_id = 'Enter your user id here'

# API settings
# Full template: http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>.
steam_api_url = 'http://api.steampowered.com/'
response_format = 'json'

# Override with your local settings, stops them being committed to GitHub
try:
    from local_settings import *
except ImportError:
    pass
