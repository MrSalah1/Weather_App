# Weather_App
Weather App
A simple terminal-based weather application that fetches and displays current weather data (temperature, humidity, and condition) for any city using the OpenWeatherMap API.
Features

Input a city name to get real-time weather information.
Displays temperature in Celsius, humidity percentage, and weather condition (e.g., "Clear sky", "Light rain").
Built with Python for ease of use and cross-platform compatibility.

Prerequisites

Python 3.11 or higher.
An active OpenWeatherMap API key (free tier available at openweathermap.org).

Installation

Clone the Repository:
git clone https://github.com/MrSalah1/weather_app.git
cd weather_app


Set Up a Virtual Environment (recommended):
python -m venv .venv
.venv\Scripts\activate  # On Windows
# On macOS/Linux: source .venv/bin/activate


Install Dependencies:
pip install requests


Obtain an API Key:

Sign up at OpenWeatherMap to get a free API key.
Store the API key in the script (Weather.py) by replacing the placeholder.



Usage

Run the script:
python Weather.py


Enter a city name (e.g., "Cairo" or "London,UK") when prompted.

View the weather data displayed in the terminal.


Example Output
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Python executable: C:\Users\modys\OneDrive\Desktop\Weather App\.venv\Scripts\python.exe
Enter city name: Cairo
Weather in Cairo:
Temperature: 29.0°C
Humidity: 55%
Condition: Clear sky

File Structure

Weather.py: The main Python script containing the weather app logic.
README.md: This file, providing project documentation.
.venv/: Virtual environment directory (if created).

Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!
License
This project is open-source. Feel free to use and modify it as needed.
Troubleshooting

401 Error: Ensure your API key is active and correctly entered. New keys may take up to 2 hours to activate.
ModuleNotFoundError: Verify requests is installed in your virtual environment.
City Not Found: Use city names with country codes (e.g., "Cairo,EG") for better accuracy.

Acknowledgements

Weather data provided by OpenWeatherMap.
