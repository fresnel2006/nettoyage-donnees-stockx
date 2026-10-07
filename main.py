import  pandas as pd
from tabulate import tabulate
import numpy as np

StockX=pd.read_csv("StockX-Data-Contest-2019-3.csv",).head(1000)

StockX["Order Date"]=pd.to_datetime(StockX["Order Date"],format="mixed")

StockX["Sale Price"]=StockX["Sale Price"].str.replace(",","").str.extract("(\d+)")[0]
StockX["Retail Price"]=StockX["Retail Price"].str.replace(",","").str.extract("(\d+)")[0]

StockX["Release Date"]=pd.to_datetime(StockX["Release Date"],format="mixed")

for i in ["Sale Price","Retail Price","Shoe Size"]:
    StockX[i]=StockX[i].astype(float)

for i in ["Buyer Region","Brand","Sneaker Name"]:
    StockX[i]=StockX[i].str.lower().str.strip()

StockX.to_csv("C:/Users/fresnel/Desktop/csv traite/StockX-Data-Contest-2019-3.csv",index=False)
print(tabulate(StockX,tablefmt="psql",headers="keys"))