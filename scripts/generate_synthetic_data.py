"""Synthetic finance and health rows for local Db2/watsonx-style analytics."""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)

portfolio = pd.DataFrame({
    "instrument_id": [f"I{i:04d}" for i in range(1, 71)],
    "sector": (["health", "finance", "tech", "energy"] * 17 + ["health", "finance"])[:70],
    "risk_score": [round(0.1 + (i % 10) * 0.08, 2) for i in range(1, 71)],
    "notional_usd": [100000 + (i * 5000) % 900000 for i in range(1, 71)],
})
portfolio.to_csv(DATA / "portfolio_positions.csv", index=False)

notes = pd.DataFrame({
    "note_id": [f"N{i:04d}" for i in range(1, 41)],
    "text": [
        "Patient stable after procedure",
        "Claim denied due to coding",
        "Quarterly revenue beat forecast",
        "MRI scheduled next week",
    ] * 10,
    "domain": ["clinical", "claims", "finance", "clinical"] * 10,
})
notes.to_csv(DATA / "unstructured_notes.csv", index=False)
print("Wrote portfolio_positions.csv and unstructured_notes.csv")
