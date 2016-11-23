from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
@app.route("/index.html")
def front():
	return render_template('index.html')

@app.route("/generic.html")
def about():
	return render_template('generic.html')

@app.route("/elements.html")
def elements():
	return render_template('elements.html')

if __name__ == "__main__":
	app.run() 