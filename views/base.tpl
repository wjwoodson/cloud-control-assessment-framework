<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html;" charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="cloud control assessment framework">
		<meta name="author" content="William Woodson <wjwoodson@gmail.com>">
		<title>cloud control assessment framework | {% block title %}{% endblock %}</title>
		<link href="static/css/bootstrap.min.css" rel="stylesheet">
		<link href="static/css/bootstrap-theme.min.css" rel="stylesheet">
	</head>
	<body>
		<div id="header">
                        {% block header %}
                        {% endblock %}
                </div>
		<div id="nav">
                        {% block nav %}
                        {% endblock %}
                </div>
		<div id="main">
                        {% block main %}
                        {% endblock %}
                </div>
		<div id="footer">
			{% block footer %}
			{% endblock %}
		</div>
		<script src="static/js/jquery-2.2.3.min.js"></script>
		<script src="static/js/bootstrap.min.js"></script>
		<script src="static/js/npm.js"></script>
	</body>
</html>
