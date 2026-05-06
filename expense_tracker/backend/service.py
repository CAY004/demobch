from datetime import datetime

from expense_tracker.ai_assistant.service import parse_transaction
from expense_tracker.database.repository import insert_transaction, load_transactions


def create_and_store_transaction(user_id: int, text: str, api_key: str | None = None):
    tx = parse_transaction(text, api_key=api_key)
    if not tx.get("date"):
        tx["date"] = datetime.utcnow().strftime("%Y-%m-%d")
    insert_transaction(user_id, tx)
    return tx


def get_user_transactions(user_id: int):
    return load_transactions(user_id)
