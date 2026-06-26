import os
import pandas as pd
import time

CACHE_DIR = "cache"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)


def get_cache_path(symbol):
    return os.path.join(CACHE_DIR, f"{symbol}.csv")


def save_cache(symbol, df):
    path = get_cache_path(symbol)
    df.to_csv(path, index=False)


def load_cache(symbol):
    path = get_cache_path(symbol)

    if os.path.exists(path):
        return pd.read_csv(path)
    return None
