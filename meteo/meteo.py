import csv
import requests
from datetime import datetime


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.6119,
        "longitude": 3.8772,
        "current_weather": "true"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def extract_weather(data):
    if "current_weather" not in data:
        raise ValueError("Réponse invalide : current_weather manquant")

    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]
    return temp, wind


def display(now, temp, wind):
    print(f"Date : {now}")
    print(f"Température : {temp}°C")
    print(f"Vent : {wind} km/h")


def write_to_csv(now, temp, wind):
    filename = "meteo.csv"
    fieldnames = ["date", "temperature", "windspeed"]

    write_header = False
    try:
        with open(filename, "r", encoding="utf-8") as f:
            if f.read(1) == "":
                write_header = True
    except FileNotFoundError:
        write_header = True

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow({
            "date": now,
            "temperature": temp,
            "windspeed": wind
        })


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        data = get_weather()
        temp, wind = extract_weather(data)
    except Exception as e:
        print("Erreur :", e)
        return

    display(now, temp, wind)
    write_to_csv(now, temp, wind)


if __name__ == "__main__":
    main()
