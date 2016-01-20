import logging
import json
from flask import request
from querystring_parser import parser

from .app import app, channels

logger = logging.getLogger(__name__)

def make_response(data, code = 200):
    return json.dumps(dict(
        result = data,
        code = code,
    )), code

@app.route('/channel/<int:pin>', methods = ['GET'])
def get_channel_value(pin):
    if pin not in channels:
        return make_response("Channel not found", 404)
    value = channels[pin].get_value()
    logger.debug("Get value '%s' from channel '%s'" % (value, pin))
    return make_response(value)

@app.route('/channel', methods = ['GET'])
def get_channels():
    res = []
    for pin in channels:
        chan = channels[pin]
        res.append(dict(
            type = chan.type,
            pin = chan.pin,
            value = chan.get_value(),
        ))
    logger.debug("List of channels (%s)" % len(channels))
    return make_response(res)

@app.route('/channel/<int:pin>', methods = ['PUT'])
def set_channel_value(pin):
    if pin not in channels:
        return make_response("Channel not found", 404)
    value = int(request.form['value'])
    channels[pin].set_value(value)
    logger.debug("Set value '%s' for channel '%s'" % (value, pin))
    return make_response('ok')

@app.route('/channel', methods = ['PUT'])
def set_channels_values():
    args = parser.parse(request.get_data())
    for pin in args['pin']:
        if pin not in channels:
            logger.error("Invalid pin number: %s" % pin)
            return make_response("Pin: '%s' not found" % pin)
        channels[pin].set_value(int(args['pin'][pin]))
    logger.debug("Set values for channels: %s" % args['pin'].keys())
    return make_response("ok")
