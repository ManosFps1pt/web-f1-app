from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Manually set the next race's date
NEXT_RACE = {
	"name": "Australian Grand Prix",
	"date": "2025-03-14",  # Check this format
}

@app.route("/")
def home():
	print("DEBUG: Race Date in Flask:", NEXT_RACE["date"])  # Print to console
	return render_template("index.html", race=NEXT_RACE)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
