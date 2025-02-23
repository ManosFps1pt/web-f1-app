from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Manually set the next race's date
NEXT_RACE = {
	"name": "Australian Grand Prix",
	"date": "2025-03-14",  # Check this format
}

counter_time = "2025-02-08 20:00"

@app.route("/")
def home():
	print("DEBUG: home page in Flask:")  # Print to console
	return render_template("index.html")


@app.route("/f1")
def f1():
	print("DEBUG: Race Date in Flask:", NEXT_RACE["date"])  # Print to console
	return render_template("f1.html", race=NEXT_RACE)

@app.route("/for-the-best-girl-in-the-world")
def app1():
	print("DEBUG: loaded timer")
	return render_template("for-my-girl.html", counter_start=counter_time)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
