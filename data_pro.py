import requests
import pandas as pd
from cache import load_cache, save_cache

class DataEnginePro:

    def format_symbol(self, symbol: str):
        symbol = symbol.strip()

        if symbol.startswith("6"):
            return symbol + ".SH"
        else:
            return symbol + ".SZ"

    def get_daily(self, symbol):

        # 🟢 1. 先读缓存（关键）
        cache_df = load_cache(symbol)
        if cache_df is not None and len(cache_df) > 10:
            return cache_df

        # 🟡 2. 请求网络
        symbol = self.format_symbol(symbol)

        url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={symbol},day,,,320,qfq"

        try:
            res = requests.get(url, timeout=8)
            data = res.json()

            klines = data.get("data", {}).get(symbol, {}).get("day", [])

            if not klines:
                return None

            df = pd.DataFrame(klines, columns=[
                "time", "open", "close", "high", "low", "volume"
            ])

            df["close"] = pd.to_numeric(df["close"])
            df["high"] = pd.to_numeric(df["high"])
            df["low"] = pd.to_numeric(df["low"])

            # 🟢 3. 写入缓存（关键）
            save_cache(symbol, df)

            return df.tail(60)

        except Exception as e:
            print("network error:", e)

            # 🔴 4. 兜底缓存
            return load_cache(symbol)
