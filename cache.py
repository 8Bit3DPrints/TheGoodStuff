import json
from typing import List

CACHE_FILE = "headline_cache.json"

def load_cached_headlines() -> List[str]:
    try:
        with open(CACHE_FILE, "r") as file:
            cache_data = json.load(file)
        return cache_data.get("headlines", [])
    except FileNotFoundError:
        return []

def save_headlines_to_cache(headlines: List[str]):
    cache_data = {"headlines": headlines}
    with open(CACHE_FILE, "w") as file:
        json.dump(cache_data, file)

