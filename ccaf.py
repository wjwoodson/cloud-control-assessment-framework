# ccaf.py - cloud control assessment framework
# Author: William Woodson <wjwoodson@gmail.com>

import logging
import imp
import json
import os
from bottle import Bottle, request, HTTPError, run, response
from controllers.ui import ui_app
from controllers.api import api_app

# Setup logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y%m%d %H%M%S', level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup bottle app
app = Bottle()

# Import routes from the UI and API
app.merge(ui_app)
app.mount("/api/1", api_app)

# Run the bottle app
run(app, host="localhost", port="8300")
