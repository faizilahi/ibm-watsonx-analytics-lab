from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"; DATA.mkdir(parents=True, exist_ok=True)
rows = []
remaining = 1842
for i in range(20):
    v = 1842 // 20 + (1 if i < 1842 % 20 else 0)
    rows.append({"clinic_id": f"C{i:02d}", "visit_date": "2024-07-15", "visits": v, "revenue": v * 120})
pd.DataFrame(rows).to_csv(DATA / "mart_clinic_daily.csv", index=False)
Path(DATA / "retrieval_answer.txt").write_text("1910\n", encoding="utf-8")
print("mart total", sum(r["visits"] for r in rows))
