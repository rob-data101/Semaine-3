import pandas as pd


def main():
    try:
        df = pd.read_csv("pokedex.csv")
    except FileNotFoundError:
        print("Fichier pokedex.csv introuvable.")
        return

    if df.empty:
        print("pokedex.csv est vide.")
        return

    # CHECK
    print("Shape :", df.shape)
    print("Colonnes :", list(df.columns))
    print(df.head())

    # 1) Top 10 Pokémon les plus lourds (par entité)
    top10 = df.drop_duplicates(subset="nom").nlargest(10, "poids_kg")
    print("\n--- Top 10 Pokémon les plus lourds ---")
    print(top10[["nom", "poids_kg", "type"]])

    # 2) Type le plus représenté
    top_type = df["type"].value_counts().idxmax()
    print("\nType le plus représenté :", top_type)

    # 3) Type le plus lourd en moyenne
    type_lourd = df.groupby("type")["poids_kg"].mean().idxmax()
    print("Type le plus lourd en moyenne :", type_lourd)

    # 4) KPI tailles globale (par Pokémon)
    kpi_taille = df.groupby("nom")["taille_cm"].agg(["mean", "max", "min"])
    print("\n--- KPI taille (cm) par Pokémon ---")
    print(kpi_taille)

    # 5) Nombre de Pokémon uniques appelés
    nb_uniques = df["nom"].nunique()

    # 6) Pokémon le plus souvent appelé
    pokemon_freq = df["nom"].value_counts().head(1)

    # 7) Nombre total d’appels API (logs)
    total_logs = len(df)

    # CONCLUSION
    print("\nCONCLUSION")
    print(f"- {nb_uniques} Pokémon uniques.")
    print(f"- Type majoritaire : {top_type}.")
    print(f"- Type le plus lourd en moyenne : {type_lourd}.")
    print(f"- Total appels API : {total_logs}.")
    print("\nPokémon le plus appelé :")
    print(pokemon_freq)


if __name__ == "__main__":
    main()
