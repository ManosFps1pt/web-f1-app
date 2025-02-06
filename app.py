from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<name>")
def welcome(name):
	return render_template("index.html", name=name)


if __name__ == "__main__":
	app.run(debug=True)

