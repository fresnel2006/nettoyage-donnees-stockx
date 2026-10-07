# Nettoyage des données StockX

Nettoyage d'un extrait du dataset **StockX Data Contest 2019** (ventes de sneakers revendues sur StockX) avec pandas.

## Ce que fait le script
- Lecture des 1000 premières lignes de `StockX-Data-Contest-2019-3.csv`
- Conversion de `Order Date` et `Release Date` en dates
- Nettoyage des prix (`Sale Price`, `Retail Price`) : suppression des symboles et virgules, passage en nombres
- Typage numérique de `Shoe Size`
- Normalisation du texte (minuscules, espaces) pour `Buyer Region`, `Brand`, `Sneaker Name`
- Export du CSV nettoyé et affichage en tableau dans la console

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Stack
Python, pandas, numpy, tabulate

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan
