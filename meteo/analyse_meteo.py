import pandas as pd

def main():
    # Lire le CSV
    df = pd.read_csv("meteo.csv")

    if df.empty:
        print("Aucune donnée météo disponible.")
        return

    print("\n--- Données brutes ---")
    print(df)

    # Trier par température
    df_sorted = df.sort_values(by="temperature", ascending=False)

    print("\n--- 3 températures les plus hautes ---")
    print(df_sorted.head(3))

    # Moyenne
    moyenne = df["temperature"].mean()
    print("\nTempérature moyenne :", moyenne)

if __name__ == "__main__":
    main()
