# Weather API Project
A beginner-friendly Python project that retrieves real-time weather information using the OpenWeather API.

## Author
Saloni Dhawale

## Features
- Search weather by city name
- Displays:
  - Temperature
  - Feels like temperature
  - Weather conditions
  - Humidity
  - Wind speed
- Handles invalid city names
- Uses environment variables to protect API keys

## Technologies Used
- Python
- Requests
- Python Dotenv
- OpenWeather API

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CheckWeatherAPI.git
cd CheckWeatherAPI
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Create a `.env` file:

```txt
API_KEY=YOUR_OPENWEATHER_API_KEY
```

Run the project:

```bash
python3 weather.py
```

## Example

```txt
Enter a city (or 'quit' to exit): Toronto

========================
Weather for Toronto
========================
Temperature: 22°C
Feels Like: 21°C
Condition: clear sky
Humidity: 58%
Wind Speed: 3.6 m/s
```

## What I Learned

- Making HTTP requests in Python
- Working with APIs
- Parsing JSON responses
- Error handling
- Using environment variables
- Managing a project with Git and GitHub

## Future Improvements

- 5-day forecast support
- Save previous searches
- Weather history
- Graphical user interface (GUI)
