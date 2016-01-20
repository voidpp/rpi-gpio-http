from flask import Flask
import logging
import logging.config
import RPi.GPIO as GPIO
from .config import config, config_loader
from .channel import ChannelFactory

app = Flask('rpi_gpio_http')

logging.config.dictConfig(config['logger'])

logger = logging.getLogger(__name__)

logger.info("Config loaded from %s" % config_loader.filename)

channels = {}

GPIO.setmode(GPIO.BOARD)

for ch in config['channels']:
    if ch['enabled'] != True:
        continue
    channel = ChannelFactory.create(ch)
    if channel:
        channels[channel.pin] = channel

import controllers
