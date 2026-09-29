# Governed SQL Mart vs Retrieval Answer

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

A watsonx-style pattern: answers must match the governed SQL mart. When
retrieval drifts, the lab flags a **mismatch** and prefers SQL.

## The mart

`mart.clinic_daily` — visits and revenue by clinic. 2024-07-15 system total
visits **1,842**.

## The question

"How many visits yesterday across all clinics?"

## The mismatch

Retrieval index returned **1,910** (stale embed). SQL mart returned **1,842**.
Emitter raises `MISMATCH` and publishes the SQL number only.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_governed.py
```
