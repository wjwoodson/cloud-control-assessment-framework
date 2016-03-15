import logging
import imp
import json
import os
from bottle import Bottle, request, HTTPError, run, response

from router import Router

# ccaf.py - cloud control assessment framework - core routing and control test module loading
# Author: William Woodson <wjwoodson@gmail.com>

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

if __name__ == "__main__":
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y%m%d %H%M%S', level=logging.INFO)
	logger = logging.getLogger(__name__)
	# Setup router
	router = Router()
	router.modules = setup_modules("./modules")
	# Setup bottle app
	app = Bottle()
	@app.hook("after_request")
	def enable_cors():
		response.headers["Access-Control-Allow-Origin"] = "*"
		response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
		response.headers["Access-Control-Allow-Headers"] = "Origin, Accept, Content-Type"
	# Return objects from the collection of control tests
	@app.route("/control_test/<name>", method=["GET"])
	@app.route("/control_test", method=["GET"])
	def control_test_get(name=None):
		if not name: name = None
		return HTTPError(501, "Not Implemented")
		#response.content_type = "application/json"
		#TODO add provider and control param filters
		#return json.dumps({}, indent=4)
	# Route requests to the selected control test module
	@app.route("/control_test/<name>", method=["PUT"])
	@app.route("/control_test", method=["PUT"])
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
	@app.route("/control_test/<name>", method=["DELETE"])
	@app.route("/control_test", method=["DELETE"])
	def control_test_delete(name=None):
		if not name: name = None
		return HTTPError(501, "Not Implemented")
		#response.content_type = "application/json"
		#TODO add provider and control param filters
                #return json.dumps({}, indent=4)

	# Return module stats
	@app.route("/stat_modules", method="GET")
	def stat_modules():
		response.content_type = "application/json"
		return json.dumps(router.stats, indent=4)
	

	# Run the bottle app
	run(app, host="localhost", port="8300")

