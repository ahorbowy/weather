from tkinter import *
from tkinter.font import Font
import requests
import json
from datetime import datetime, date
from key import api_key  # import api key

# Lista miast których pogodę można sprawdzić (miasta wojewódzkie)
cities = [
    "Białystok",
    "Bydgoszcz",
    "Gdańsk",
    "Gorzów Wielkopolski",
    "Katowice",
    "Kielce",
    "Kraków",
    "Lublin",
    "Łódź",
    "Olsztyn",
    "Opole",
    "Poznań",
    "Rzeszów",
    "Szczecin",
    "Toruń",
    "Warszawa",
    "Wrocław",
    "Zielona Góra",
]

# Funkcja do pobierania aktualnej daty i godziny


def get_time_and_date():
    time = datetime.now()
    day = date.today()
    timeLabel.config(text=f"Time:\n{time.strftime("%X")}")
    timeLabel.after(1000, get_time_and_date)
    dateLabel.config(text=day)

# Funkcja do pobierania danych o pogodzie


def fetch_weather(*args):
    city = currentCity.get()  # pobranie aktualnego miasta
    api = requests.get(  # wywołanie API
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/today?unitGroup=metric&include=current&key={api_key}&contentType=json")
    try:
        weather = api.json()  # Przetworzenie wyniku na format JSON
    except json.decoder.JSONDecodeError:
        print("Incorrect format")
    else:
        # Wyświetlenie odpowiednich wartości dotyczących pogody
        for temp in weather["days"]:
            currentCityTempLabel.config(
                text=f"Temperature:\n{temp["temp"]} °C")
            sunriseLabel.config(
                text=f"Sunrise:\n{temp["sunrise"]} AM")
            sunsetLabel.config(
                text=f"Sunset:\n{temp["sunset"]} PM")
            pressureLabel.config(
                text=f"Pressure:\n{temp["pressure"]} hPa")
            windspeedLabel.config(
                text=f"Windspeed:\n{temp["windspeed"]} km/h")
            conditionDescriptionLabel.config(
                text=f"Daily weather description:\n{temp["description"]}")


# Główne okno tkinter
if __name__ == "__main__":
    window = Tk()
    font_style = Font(family="Helvetica", size=12,
                      weight="bold")  # style czcionki
    bg_color = "#87898c"  # kolor tła
    window.title("Weather")  # tytuł okna
    window.geometry("400x250")  # wymiary okna
    window.resizable(False, False)  # blokada zmiany rozmiaru
    window.config(bg=bg_color)

    # definicja zmiennej przechowującej aktualnie wybrane miasto
    currentCity = StringVar()
    currentCity.set(cities[15])  # ustawienie domyślnego miasta na "Warszawa"
    # śledzenie zmiany miasta oraz w przypadku zmiany, wywołanie funkcji fetch_weather
    currentCity.trace_add("write", fetch_weather)

    # definicja menu z wyborem miasta
    cityMenu = OptionMenu(window, currentCity, *cities)
    cityMenu.config(font=font_style, bg=bg_color)
    cityMenu.pack()

    # definicja etykiet wyświetlających odpowiednie dane
    dateLabel = Label(window, font=font_style, bg=bg_color)
    dateLabel.place(x=0, y=0)

    timeLabel = Label(window, font=font_style, bg=bg_color)
    timeLabel.place(x=24, y=55)

    currentCityTempLabel = Label(window, font=font_style, bg=bg_color)
    currentCityTempLabel.place(x=10, y=95)

    sunriseLabel = Label(window, font=font_style, bg=bg_color)
    sunriseLabel.place(x=148, y=55)

    sunsetLabel = Label(window, font=font_style, bg=bg_color)
    sunsetLabel.place(x=148, y=95)

    pressureLabel = Label(window, font=font_style, bg=bg_color)
    pressureLabel.place(x=280, y=55)

    windspeedLabel = Label(window, font=font_style, bg=bg_color)
    windspeedLabel.place(x=280, y=95)

    conditionDescriptionLabel = Label(
        window, font=font_style, wraplength=250, bg=bg_color)
    conditionDescriptionLabel.place(x=90, y=145)
    # wywołanie funkcji
    fetch_weather()
    get_time_and_date()
    # pętla głowna aplikacji
    window.mainloop()
