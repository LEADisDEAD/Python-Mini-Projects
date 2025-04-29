import tkinter as tk
import requests
from tkinter import messagebox


API_KEY = "2cf84b05af41ff2f70cfdec67af3f72b"


def get_weather_data(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()


    return {
        'city': data['name'],
        'country': data['sys']['country'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        weather = get_weather_data(city, API_KEY)

        result_label.config(
            text=f"{weather['city']}, {weather['country']}\n"
                 f"🌡️ {weather['temperature']}°C\n"
                 f"☁️ {weather['description'].capitalize()}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch weather data.\n{e}")




# UI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), justify='center')
city_entry.pack(pady=5)

search_btn = tk.Button(root, text="Get Weather", command=show_weather, font=("Arial", 12), bg="skyblue")
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

root.mainloop()
