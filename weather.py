import requests

API_KEY = "6907c2c9a86fc8ca3f33e612e072258b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    print("🔎 Debug URL:", response.url)
    print("📡 Status Code:", response.status_code)

    try:
        data = response.json()
    except Exception as e:
        print("❌ Failed to parse JSON:", e)
        return

    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"\n📍 Weather in {city.title()}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Description: {description.capitalize()}")
    else:
        print("\n❌ City not found or error in request.")
        print("📩 Full response:", data)

# Run it
city = input("Enter city name: ")
get_weather(city)
