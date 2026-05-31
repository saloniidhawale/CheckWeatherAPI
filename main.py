# When you run: python3 weather.py
#  the program:
#  Asks the user for a city
#  Sends a request to OpenWeather
#  Receives weather data
#  Extracts useful information
#  Prints it nicely
#  Repeats until the user types "quit"

import requests # Allows Python to communicate with websites and APIs
import os # Lets Python interact with your computer's environment. *Anyone viewing your GitHub can steal your key
from dotenv import load_dotenv # Reads your .env file

load_dotenv() # "Read the .env file and load its contents" Without this, Python would never know the variable exists.

API_KEY = os.getenv("API_KEY") # "*"

if not API_KEY:
    print("Error: API_KEY not found in .env file")
    exit()

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5) # This sends a GET request to Google. computer talks to OpenWeather
        data = response.json() # converts JSON into a Python dictionary

        if response.status_code != 200:
            print(f"\nError: {data.get('message', 'Unknown error')}")
            return

        print("\n========================") #everything returned in JSON, python dictionary
        print(f"Weather for {data['name']}")
        print("========================")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Condition: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

while True:
    city = input("\nEnter a city (or 'quit' to exit): ").strip()

    if city.lower() == "quit":
        print("Goodbye!")
        break

    if not city:
        print("Please enter a city name.")
        continue

    get_weather(city)