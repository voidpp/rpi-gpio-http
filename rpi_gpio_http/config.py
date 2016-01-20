import os
from voidpp_tools.json_config import JSONConfigLoader

config_loader = JSONConfigLoader(os.path.dirname(__file__))

config = config_loader.load('rpi-gpio-http-config.json')
