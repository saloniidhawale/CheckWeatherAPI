from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY_HERE"

@app.route("/")
def home():

    city = "Toronto"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url, timeout=5)

    print("STATUS CODE:", response.status_code)
    print("TEXT RESPONSE:", response.text)

    return response.text


if __name__ == "__main__":
    app.run(debug=True)