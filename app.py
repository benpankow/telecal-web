from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
	page = request.args.get("page")
	if page == None:
		page = "five"
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}. {page}</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time, page=page)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
