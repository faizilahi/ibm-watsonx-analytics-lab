"""Rule-based NLP stand-in for watsonx classification demos."""
import pandas as pd
from pathlib import Path

RULES = {
    "clinical": ["patient", "mri", "procedure", "stable"],
    "claims": ["claim", "denied", "coding"],
    "finance": ["revenue", "forecast", "quarter"],
}

def classify_notes(root: Path):
    df = pd.read_csv(root / "data" / "unstructured_notes.csv")
    labels = []
    for text in df["text"].str.lower():
        scores = {k: sum(w in text for w in words) for k, words in RULES.items()}
        labels.append(max(scores, key=scores.get))
    df["predicted_domain"] = labels
    out = root / "data" / "notes_classified.csv"
    df.to_csv(out, index=False)
    print(df.head())
    print(f"Wrote {out}")
