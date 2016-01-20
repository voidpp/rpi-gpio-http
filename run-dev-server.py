
from rpi_gpio_http.app import app

app.debug = True

app.run('0.0.0.0', 5000, threaded = True, use_reloader = True, use_debugger = True)
