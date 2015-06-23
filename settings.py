__author__ = 'Luke Merrett'

steam_webapi_key = 'Get your key here http://steamcommunity.com/dev'
registered_domain = 'The domain used to register above'

# Override with your local settings, stops them being committed to GitHub
try:
    from local_settings import *
except ImportError:
    pass
