from tkinter import Tk
from tkinter.font import Font
from weather_app import WeatherApp

if __name__ == "__main__":
    window = Tk()  # Inicjalizacja głównego okna aplikacji
    font_style = Font(family="Helvetica", size=12,
                      weight="bold")
    # Utworzenie instancji klasy WeatherApp
    app = WeatherApp(window, font_style)
    window.mainloop()  # Pętla główna tkinter
