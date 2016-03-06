import logging
import time

logger = logging.getLogger(__name__)
class Router:
	"""Router - Route requests to the appropriate control test module
	"""
	def __init__(self):
		self.modules = {}
		self.stats = {
			"total"   : 0,
			"average" : 0,
			"modules" : {}
		}

	def _execute_module(self, request, module):
		"""_execute_module(request, route) - Execute a module
			
			Output: A Result Object in the format:
			{
				"module" : name (string)
				"data"	 : module response data (string)
				"took"   : time taken in seconds (int)
			}
		"""
		result = {}
		if module.match(request):
			# Start the timer for 'took'
			start_time = time.time()
			output = ""
			# Try to process the request
			try:
				output = module.run(request)
			except Exception as e:
				output = "Error {0}".format(str(e))
				logger.error(str(e))
			# Stop the timer for 'took'
			took = int ((time.time()-start_time)*1000)
			# Add to stats
			if module.name not in self.stats:
				self.stats["modules"][module.name] = 1
			else:
				self.stats["modules"][module.name] += 1
			# Finalize the module result
			result = {
				"module" : module.name,
				"data"   : str(output),
				"took"   : took
			}
		return result

	def handle(self, request, module_name=None):
		"""handle(request) - Check for matching module and process the request
		"""
		print self.modules
		self.stats["total"] += 1
		# Create the base response
		response = {
			"_metadata" : {
				"match_count" : 0,
				"modules" : [],
				"took" : 0
			},
			"results" : []
		}
		if not module_name: module_name = None
		# If a module was specified, just run it
		if module_name:
			if module_name not in self.modules:
				return response
			result = self._execute_module(request, self.modules.get(module_name))
			if result:
				# Finalize the result
				response["_metadata"]["match_count"] += 1
				response["_metadata"]["modules"].append(module_name)
				response["_metadata"]["took"] += result["took"]
				response["results"].append(result)
		else:
			for module in self.modules.values():
				# Try to process the request
				result = self._execute_module(request, module)
				if result:
					# Finalize the result
					response["_metadata"]["match_count"] += 1
					response["_metadata"]["modules"].append(module.name)
					response["_metadata"]["took"] += result["took"]
					response["results"].append(result)
		return response

	def validate(self, request):
		"""validate(request) - Ensure the request contains a valid request object
		"""
		return True
