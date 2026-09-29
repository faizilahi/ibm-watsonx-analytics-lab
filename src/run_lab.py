"""Analytics SQL + optional rule NLP classify."""
from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parents[1]
con = duckdb.connect(str(ROOT / "ibm_analytics.duckdb"))
con.execute("CREATE OR REPLACE TABLE positions AS SELECT * FROM read_csv_auto(?)", [str(ROOT / "data" / "portfolio_positions.csv")])
con.execute("CREATE OR REPLACE TABLE notes AS SELECT * FROM read_csv_auto(?)", [str(ROOT / "data" / "unstructured_notes.csv")])
print("=== High risk health sector ===")
print(con.execute("""
SELECT instrument_id, risk_score, notional_usd
FROM positions WHERE sector='health' AND risk_score >= 0.5
ORDER BY risk_score DESC LIMIT 10
""").fetchdf())
from src.rule_nlp import classify_notes
classify_notes(ROOT)
