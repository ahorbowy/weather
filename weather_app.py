from tkinter import StringVar, OptionMenu, Label
from datetime import datetime
from weather_data import WeatherData
from cities import cities


class WeatherApp:
    """
    Klasa reprezentująca interfejs użytkownika apki pogodowej
    """

    def __init__(self, window, font_style):
        # Inicjalizacja interfejsu użytkownika
        self.window = window
        self.font_style = font_style
        self.bg_color = "#87898c"
        self.window.title("Weather")
        self.window.geometry("400x250")
        self.window.resizable(False, False)
        self.window.config(bg=self.bg_color)
        # Zmienna przechowująca aktualnie wybrane miasto
        self.current_city = StringVar()
        self.current_city.set("Warszawa")
        # Wywołanie metody fetch_weather przy zmianie wybranego miasta
        self.current_city.trace_add("write", self.fetch_weather)

        # Menu rozwijane z wyborem miasta
        self.city_menu = OptionMenu(
            self.window, self.current_city, *cities)
        self.city_menu.config(font=self.font_style, bg=self.bg_color)
        self.city_menu.pack()

        # Etykiety wyświetlające dane pogodowe
        self.date_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.date_label.place(x=15, y=75)

        self.time_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.time_label.place(x=24, y=55)

        self.current_city_temp_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.current_city_temp_label.place(x=10, y=95)
        self.sunrise_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.sunrise_label.place(x=148, y=55)
        self.sunset_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.sunset_label.place(x=148, y=95)
        self.pressure_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.pressure_label.place(x=280, y=55)
        self.windspeed_label = Label(
            self.window, font=self.font_style, bg=self.bg_color)
        self.windspeed_label.place(x=280, y=95)
        self.condition_description_label = Label(
            self.window, font=self.font_style, wraplength=250, bg=self.bg_color)
        self.condition_description_label.place(x=90, y=145)

        self.fetch_weather()  # Wywołanie metody fetch_weather
        self.update_clock()  # Wywołanie metody update_clock

    def fetch_weather(self, *args):
        # Pobieranie danych pogodowych dla wybranego miasta
        city = self.current_city.get()
        weather_data = WeatherData(city)
        weather = weather_data.fetch_weather()

        # Aktualizacja etykiet z danymi pogodowymi
        self.current_city_temp_label.config(
            text=f"Temperature:\n{weather['temp']} °C")
        self.sunrise_label.config(
            text=f"Sunrise:\n{weather['sunrise']} AM")
        self.sunset_label.config(
            text=f"Sunset:\n{weather['sunset']} PM")
        self.pressure_label.config(
            text=f"Pressure:\n{weather['pressure']} hPa")
        self.windspeed_label.config(
            text=f"Windspeed:\n{weather['windspeed']} km/h")
        self.condition_description_label.config(
            text=f"Daily weather description:\n{weather['description']}")

    def update_clock(self):
        # Aktualizacja etykiety z datą i czasem w czasie rzeczywistym
        now = datetime.now()
        self.date_label.config(text=now.strftime("%Y-%m-%d"))
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        # Wywołanie metody co 1 sekundę
        self.window.after(1000, self.update_clock)
