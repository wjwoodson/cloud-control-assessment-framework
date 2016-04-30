# ui.py - cloud control assessment framework - ui templates and static resources
# Author: William Woodson <wjwoodson@gmail.com>

import logging
import imp
from bottle import Bottle, request, static_file, TEMPLATE_PATH, jinja2_template as template, HTTPError

# Setup logging
logger = logging.getLogger(__name__)

# Setup bottle app
ui_app = Bottle()

# Home page
@ui_app.route("/")
def home():
	return template('home') 

# Serve static content
@ui_app.route('/static/<filepath:path>')
def static_content(filepath):
	return static_file(filepath, root='./views/static')
