name = "sample_module"
"""sample_module - Sample control test module demonstrating required functions
"""

def match(request):
	"""match(request) - Match conditions in order for module to be run
	"""
	if request.method == "PUT":
		return True
	return False

def run(request):
	"""run(request) - Execute module and return a string
	"""
	return 'sample module complete'
