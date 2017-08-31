from flask import Flask
from flask import request
from datetime import datetime
app = Flask(__name__)

results = []

@app.route('/')
def homepage():
	global results
	code = request.args.get("code")
	if code != None and not code in results:
		results += code
	return """Thank you, you are now authorized!"""

@app.route('/results/')
def res():
	s = ''
	for r in results:
		s = s + r
	return s

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
