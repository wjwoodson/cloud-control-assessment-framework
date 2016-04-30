# api.py - cloud control assessment framework - core routing and control test module loading
# Author: William Woodson <wjwoodson@gmail.com>

import logging
import imp
import json
import os
from bottle import Bottle, request, HTTPError, run, response
from controllers.router import Router
from models.framework import get_framework

class InvalidRouteException(Exception):
	"""InvalidRouteException
	"""
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return repr(self.msg)

def setup_modules(module_dir):
	"""setup_modules(module_dir) - Search for control test modules in the provided directory
	"""
	modules = {}
	entries = os.listdir(module_dir)
	for entry in entries:
		path = os.path.join(module_dir, entry)
		# Make sure there's an __init__.py in each module directory
		if not os.path.isdir(path) or not "__init__.py" in os.listdir(path):
			continue
		fp, pathname, description = imp.find_module("__init__", [path])
		try:
			logger.info("[+] Loading module: {0}".format(entry))
			module = imp.load_module(entry, fp, pathname, description)
			# Make sure the module is valid
			# Make sure it has "match", "run" functions and returns standard results
			for required_func in ["match", "run"]:
				if not hasattr(module, required_func):
					raise InvalidRouteException("Missing required function {0}".format(required_func))
				if not hasattr(getattr(module, required_func), "__call__"):
					raise InvalidRouteException("Required function {0} not callable".format(required_func))
			# Check to make sure each module is named, else give it the name of the directory
			if not hasattr(module, "name"):
				module.name = entry
			modules[module.name] = module
		except Exception as e:
			logger.error("Error loading module {0}: {1}".format(path, str(e)))
		finally:
			if fp:
				fp.close()
	return modules


# Setup logging
logger = logging.getLogger(__name__)

# Setup router
router = Router()
router.modules = setup_modules("./modules")

# Setup bottle app
api_app = Bottle()

# Providers
# Return objects from the collection of providers
@api_app.route("/provider/<name>", method=["GET"])
@api_app.route("/provider/", method=["GET"])
@api_app.route("/provider", method=["GET"])
def provider_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Add an object to the collection of providers
@api_app.route("/provider/", method=["POST"])
@api_app.route("/provider", method=["POST"])
def provider_post():
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Update an object in the collection of providers
@api_app.route("/provider/<name>", method=["PUT"])
def provider_put(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Delete objects from the collection of providers
@api_app.route("/provider/<name>", method=["DELETE"])
@api_app.route("/provider/", method=["DELETE"])
@api_app.route("/provider", method=["DELETE"])
def provider_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
	# Frameworks
# Return objects from the collection of frameworks
@api_app.route("/framework/<name>", method=["GET"])
@api_app.route("/framework/", method=["GET"])
@api_app.route("/framework", method=["GET"])
def framework_get(name=None):
	if not name: name = None
	response.content_type = "application/json"
	return json.dumps(get_framework(name), indent=4)
# Add an object to the collection of frameworks
@api_app.route("/framework/", method=["POST"])
@api_app.route("/framework", method=["POST"])
def framework_post():
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Update an object in the collection of frameworks
@api_app.route("/framework/<name>", method=["PUT"])
def framework_put(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Delete objects from the collection of frameworks
@api_app.route("/framework/<name>", method=["DELETE"])
@api_app.route("/framework/", method=["DELETE"])
@api_app.route("/framework", method=["DELETE"])
def framework_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)

# Threats
# Return objects from the collection of threats
@api_app.route("/threat/<name>", method=["GET"])
@api_app.route("/threat/", method=["GET"])
@api_app.route("/threat", method=["GET"])
def threat_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add framework param filter
	#TODO add with_controls and with_rels param bools
	#return json.dumps({}, indent=4)
# Add an object to the collection of threats
@api_app.route("/threat/", method=["POST"])
@api_app.route("/threat", method=["POST"])
def threat_post(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Update an object in the collection of threats
@api_app.route("/threat/<name>", method=["PUT"])
def threat_put(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Delete objects from the collection of threats
@api_app.route("/threat/<name>", method=["DELETE"])
@api_app.route("/threat/", method=["DELETE"])
@api_app.route("/threat", method=["DELETE"])
def threat_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add framework param filter
	#return json.dumps({}, indent=4)

# Controls
# Return objects from the collection of controls
@api_app.route("/control/<name>", method=["GET"])
@api_app.route("/control/", method=["GET"])
@api_app.route("/control", method=["GET"])
def control_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add framework param filter
	#TODO add with_threats and with_rels param bools
	#return json.dumps({}, indent=4)
# Add an object to the collection of controls
@api_app.route("/control/", method=["POST"])
@api_app.route("/control", method=["POST"])
def control_post(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Update an object in the collection of controls
@api_app.route("/control/<name>", method=["PUT"])
def control_put(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Delete objects from the collection of controls
@api_app.route("/control/<name>", method=["DELETE"])
@api_app.route("/control/", method=["DELETE"])
@api_app.route("/control", method=["DELETE"])
def control_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add framework param filter
	#return json.dumps({}, indent=4)

# Assessments
# Return objects from the collection of assessments
@api_app.route("/assessment/<name>", method=["GET"])
@api_app.route("/assessment/", method=["GET"])
@api_app.route("/assessment", method=["GET"])
def assessment_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add full_report, with_threats, with_control_tests, with_framework param bools
	#TODO add format param (json,html,pdf)
	#return json.dumps({}, indent=4)
# Add an object to the collection of assessments
@api_app.route("/assessment/", method=["POST"])
@api_app.route("/assessment", method=["POST"])
def assessment_post(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
# Update an object in the collection of asessments
@api_app.route("/assessment/<name>", method=["PUT"])
def assessment_put(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)
	# Delete objects from the collection of assessments
@api_app.route("/assessment/<name>", method=["DELETE"])
@api_app.route("/assessment/", method=["DELETE"])
@api_app.route("/assessment", method=["DELETE"])
def assessment_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#return json.dumps({}, indent=4)

# Control Tests
# Return objects from the collection of control tests
@api_app.route("/control_test/<name>", method=["GET"])
@api_app.route("/control_test/", method=["GET"])
@api_app.route("/control_test", method=["GET"])
def control_test_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add provider and control param filters
	#return json.dumps({}, indent=4)
# Route requests to the selected control test module
@api_app.route("/control_test/<name>", method=["PUT"])
@api_app.route("/control_test/", method=["PUT"])
@api_app.route("/control_test", method=["PUT"])
def control_test_put(name=None):
	if not name: name = None
	if router.validate(request):
		try:
			response.content_type = "application/json"
			return json.dumps(router.handle(request, module_name=name), indent=4)
		except Exception as e:
			logger.error("Error handling request: {0}".format(str(e)))
	else:
		return HTTPError(400, "Bad Request")
# Delete objects from the collection of the control tests
@api_app.route("/control_test/<name>", method=["DELETE"])
@api_app.route("/control_test/", method=["DELETE"])
@api_app.route("/control_test", method=["DELETE"])
def control_test_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add provider and control param filters
	#return json.dumps({}, indent=4)

# Control Test Results
# Return objects from the collection of control test results
@api_app.route("/control_test_result/<name>", method=["GET"])
@api_app.route("/control_test_result/", method=["GET"])
@api_app.route("/control_test_result", method=["GET"])
def control_test_result_get(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add provider and control param filters
	#return json.dumps({}, indent=4)
# Delete objects from the collection of control test results
@api_app.route("/control_test_result/<name>", method=["DELETE"])
@api_app.route("/control_test_result/", method=["DELETE"])
@api_app.route("/control_test_result", method=["DELETE"])
def control_test_result_delete(name=None):
	if not name: name = None
	return HTTPError(501, "Not Implemented")
	#response.content_type = "application/json"
	#TODO add provider and control param filters
	#return json.dumps({}, indent=4)
# Utils
# Return module stats
@api_app.route("/stat_modules/", method="GET")
@api_app.route("/stat_modules", method="GET")
def stat_modules():
	response.content_type = "application/json"
	return json.dumps(router.stats, indent=4)
