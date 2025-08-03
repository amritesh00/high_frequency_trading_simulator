# app/utils.py
import os

def validate_key(api_key):
    expected = os.getenv("API_KEY", "demo123")
    return api_key == expected
