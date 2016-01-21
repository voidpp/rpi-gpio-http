About
------
This is a REST api for GPIO ports in Raspberry P.

REST api
--------

**Format**:

+ request: "application/x-www-form-urlencoded"
+ response: json

**Endpoints**:

+ ``GET /channel`` *List of all enabled channels, and their values*
+ ``PUT /channel`` *Set values* Example: ``value[11]=100&value[13]=100&value[15]=100``
+ ``GET /channel/10`` *Get the value of the 10th channel*
+ ``PUT /channel/10`` *Set the value of the 10th channel. Not available for "input". PWM: [0, 100]. Output: [0, 1]* Example: ``value=10``

Config
------
See example configuration. (rpi-gpio-http-config.example.json) It contains all the available channel types.

Type config:

+ **output**: none
+ **input**: pull: up|down: see http://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
+ **pwm**: frequency: in Hz

*Note: pin numbers is the physical number in the board*

Install
-------
``pip install rpi-gpio-http``

Do not use the ``run-dev-server.py`` in 'production', instead of this use `uWSGI <https://uwsgi-docs.readthedocs.org/en/latest/>`_, or sg else.
