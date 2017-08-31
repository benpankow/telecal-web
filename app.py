from flask import Flask
from flask import request
from datetime import datetime
app = Flask(__name__)

results = []

@app.route('/')
def homepage():
	global results
	code = request.args.get("code")
	user = request.args.get("state")
	if code != None and not code in results and user != None:
		results.append((user, code))
	return """Thank you, you are now authorized!"""

@app.route('/results/')
def res():
	s = ''
	for r in results:
		s = s + r[0] + "," + r[1] + "\n"
	return s

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
