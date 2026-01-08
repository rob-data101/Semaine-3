from datetime import datetime
import json
import os


def main():
    filename = "examples/email_support_tech1.txt"
    stop_words = ["merci", "cordialement", "bien à vous"]

    if not os.path.exists(filename):
        print("Fichier introuvable :", filename)
        return

    lignes_propres = []

    with open(filename, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            low = ligne.lower()

            if ligne == "":
                continue

            if "envoyé depuis" in low:
                continue

            if "@" in ligne:
                continue

            # stop: coupe tout à partir de la formule de fin
            if any(w in low for w in stop_words):
                break

            lignes_propres.append(ligne)

    texte_propre = "\n".join(lignes_propres)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tokens = texte_propre.lower().split()
    stoplist = {"bonjour", "vous", "pour", "avec", "plus", "comme", "depuis"}

    keywords = []
    seen = set()

    for mot in tokens:
        mot = mot.strip(".,!?;:\"'()[]").lower()

        if len(mot) <= 4:
            continue

        if mot in stoplist:
            continue

        if mot in seen:
            continue

        seen.add(mot)
        keywords.append(mot)

        if len(keywords) == 5:
            break

    result = {
        "clean_text": texte_propre,
        "source": "email",
        "keywords": keywords,
        "timestamp": now
    }

    # écrire JSON (1 fichier par email)
    os.makedirs("json", exist_ok=True)

    base = os.path.splitext(os.path.basename(filename))[0]
    output_path = f"json/output_{base}.json"

    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(result, out, ensure_ascii=False, indent=2)

    print("✅ JSON généré :", output_path)
    print(result)


if __name__ == "__main__":
    main()
