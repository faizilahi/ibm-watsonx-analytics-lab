import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from mart import sql_visits
from retrieval_answer import retrieve
from govern import reconcile
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    sql_v = sql_visits(DATA / "mart_clinic_daily.csv", "2024-07-15")
    ret_v = retrieve(DATA / "retrieval_answer.txt")
    result = reconcile(sql_v, ret_v)
    result["question"] = "How many visits yesterday across all clinics?"
    pd.DataFrame([result]).to_csv(OUT / "governed_answer.csv", index=False)
    print(json.dumps(result, indent=2))
if __name__ == "__main__":
    main()
