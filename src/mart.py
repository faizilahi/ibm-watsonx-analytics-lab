import pandas as pd
from pathlib import Path

def sql_visits(mart_path: Path, day: str) -> int:
    df = pd.read_csv(mart_path)
    return int(df.loc[df["visit_date"] == day, "visits"].sum())
