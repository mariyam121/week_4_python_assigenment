import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\n--- WEATHER INFORMATION ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("Error:", data.get("message", "Unable to get weather."))

except Exception as e:
    print("Error:", e)