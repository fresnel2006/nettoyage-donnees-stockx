from pathlib import Path

import pandas as pd
from tabulate import tabulate

DOSSIER = Path(__file__).parent
SORTIE = DOSSIER / "output"
SORTIE.mkdir(exist_ok=True)

stockx = pd.read_csv(DOSSIER / "StockX-Data-Contest-2019-3.csv").head(1000)

# Dates
stockx["Order Date"] = pd.to_datetime(stockx["Order Date"], format="mixed")
stockx["Release Date"] = pd.to_datetime(stockx["Release Date"], format="mixed")

# Prix : "$1,097" -> 1097.0 (les centimes sont gardés s'il y en a)
for colonne in ["Sale Price", "Retail Price"]:
    stockx[colonne] = (
        stockx[colonne]
        .str.replace(r"[$,\s]", "", regex=True)
        .astype(float)
    )

stockx["Shoe Size"] = stockx["Shoe Size"].astype(float)

# Texte : minuscules et espaces en trop
for colonne in ["Buyer Region", "Brand", "Sneaker Name"]:
    stockx[colonne] = stockx[colonne].str.lower().str.strip()

stockx.to_csv(SORTIE / "stockx_nettoye.csv", index=False)
print(tabulate(stockx, tablefmt="psql", headers="keys", showindex=False))
