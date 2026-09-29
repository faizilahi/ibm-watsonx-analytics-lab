def reconcile(sql_value: int, retrieval_value: int) -> dict:
    if sql_value != retrieval_value:
        return {
            "status": "MISMATCH",
            "published_value": sql_value,
            "sql_value": sql_value,
            "retrieval_value": retrieval_value,
            "action": "prefer_sql_mart",
        }
    return {"status": "OK", "published_value": sql_value, "sql_value": sql_value, "retrieval_value": retrieval_value}
