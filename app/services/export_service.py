import pandas as pd

def export_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

def export_excel(df: pd.DataFrame, path: str):
    df.to_excel(path, index=False)
