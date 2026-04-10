import pandas as pd
import os

DATA_PATH = "data/raw"

def extrair_dados():
    arquivos = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]
    dfs = []
    for arquivo in arquivos:
        df = pd.read_csv(os.path.join(DATA_PATH, arquivo))
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def normalizar_produto(nome):
    nome = str(nome).lower().strip()
    mapping = {
        "rg35xx": ["rg-35xx", "anbernic 35"]
    }
    for canonico, variacoes in mapping.items():
        if nome == canonico or nome in variacoes:
            return canonico
    return nome

def transformar_dados(df):
    print("🧹 Limpando dados...")
    df = df.drop_duplicates()
    df.columns = [c.lower() for c in df.columns]
    if "product" in df.columns:
        df["product"] = df["product"].apply(normalizar_produto)
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna()
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/clean_data.csv", index=False)
    return df
