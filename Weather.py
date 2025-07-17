
import requests

def get_weather(city):
    api_key = "f2ecea6242c8fce463588ba26ec2d10a"  # OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract relevant data
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        # Display weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("City not found or invalid response from API.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)