# 🚀 Semaine 3 – IA & Automation Sprint

(Python • API • CSV • pandas • Parsing)

## 📘 Compétences travaillées

- Bases Python appliquées (fonctions, boucles, conditions, fichiers)
- Appels API REST avec `requests`
- Parsing et transformation de JSON
- Structuration de scripts Python (séparation des responsabilités)
- Persistance des données (CSV, JSON)
- Analyse de données avec pandas
- Préparation de données non structurées pour l’IA

---

## 🔧 Projets réalisés

### 1️⃣ Scripts API – Collecte de données

- Appel d’API REST (Open-Meteo, PokéAPI)
- Extraction des champs utiles depuis des JSON imbriqués
- Horodatage des données
- Logging en CSV exploitable (Excel, pandas, BI)

➡️ Objectif : maîtriser le pipeline **API → données exploitables**.

---

### 2️⃣ Analyse de données (pandas)

- Lecture de fichiers CSV générés par les scripts
- Nettoyage logique des données (logs vs entités)
- Statistiques simples et KPIs
- Tri, regroupement, déduplication

➡️ Passage de la collecte brute à l’analyse utile.

---

### 3️⃣ Parsing d’email → JSON

- Lecture d’un email brut (texte non structuré)
- Nettoyage du bruit (signatures, métadonnées)
- Extraction de mots-clés (règles simples)
- Export structuré en JSON (1 email = 1 fichier)

➡️ Base de préparation pour intégration IA (résumé, classification, automatisation).

---

## 📂 Dossiers

- `/meteo` → script API météo + analyse
- `/pokemon` → script PokéAPI + analyse pandas
- `/email-parser` → parsing d’emails vers JSON

---

## 🎯 Objectif Semaine 4

Appliquer l’IA sur ces bases Python :
- résumé automatique
- classification intelligente
- recommandations d’actions  
→ début d’un **assistant IA complet et pilotable**.

📄 Voir `notes.md` pour le retour global.
