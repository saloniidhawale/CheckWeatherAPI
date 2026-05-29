from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "b2d46888125f3687d51c8d0316bd6575"

@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        weather_data = {
            "city": city,
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"]
        }

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)