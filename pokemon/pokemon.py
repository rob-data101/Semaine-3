import requests
import csv
from datetime import datetime


def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/machamp"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def extract_pokemon(data):
    name = data["name"]

    # PokéAPI : height = décimètres / weight = hectogrammes
    height_cm = data["height"] * 10
    weight_kg = data["weight"] / 10

    type_ = data["types"][0]["type"]["name"]
    return name, height_cm, weight_kg, type_


def display(name, height_cm, weight_kg, type_):
    print(f"Nom : {name}")
    print(f"Taille : {height_cm} cm")
    print(f"Poids : {weight_kg} kg")
    print(f"Type principal : {type_}")


def write_to_csv(now_str, name, height_cm, weight_kg, type_):
    filename = "pokedex.csv"
    fieldnames = ["date", "nom", "taille_cm", "poids_kg", "type"]

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
            "date": now_str,
            "nom": name,
            "taille_cm": height_cm,
            "poids_kg": weight_kg,
            "type": type_
        })


def main():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = get_pokemon()
    name, height_cm, weight_kg, type_ = extract_pokemon(data)
    display(name, height_cm, weight_kg, type_)
    write_to_csv(now_str, name, height_cm, weight_kg, type_)


if __name__ == "__main__":
    main()
