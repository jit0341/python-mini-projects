import tkinter as tk
import requests

API_KEY = '9c9f6ab454b8f43cee53f399862413b8'

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        result = f"City: {city}\nTemperature: {temp}°C\nWeather: {weather}"
    else:
        result = "City not found."
    
    result_label.config(text=result)

# --- GUI Setup ---
app = tk.Tk()
app.title("Weather App")
app.geometry("300x200")

city_entry = tk.Entry(app, width=25)
city_entry.pack(pady=10)

get_button = tk.Button(app, text="Get Weather", command=get_weather)
get_button.pack(pady=5)

result_label = tk.Label(app, text="", wraplength=250, justify="left")
result_label.pack(pady=10)

app.mainloop()