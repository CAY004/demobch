import json
import os
from openai import OpenAI


def parse_transaction(text: str, api_key: str | None = None) -> dict:
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Missing OpenAI API key. Add key in sidebar or set OPENAI_API_KEY.")
    client = OpenAI(api_key=key)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": "Extract finance transaction to strict JSON keys: date, amount, type, category, description. date format YYYY-MM-DD."},
            {"role": "user", "content": text},
        ],
    )
    return json.loads(response.output_text.strip())
