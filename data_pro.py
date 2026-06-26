import requests
import pandas as pd

class DataEnginePro:

    def format_symbol(self, symbol: str):

        symbol = symbol.strip()

        # 自动补交易所后缀（关键修复）
        if symbol.startswith("6"):
            return symbol + ".SH"
        else:
            return symbol + ".SZ"

    def get_daily(self, symbol):

        symbol = self.format_symbol(symbol)

        url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={symbol},day,,,320,qfq"

        try:
            res = requests.get(url, timeout=8)
            data = res.json()

            # 安全取值（关键）
            klines = data.get("data", {}).get(symbol, {}).get("day", [])

            if not klines:
                return None

            df = pd.DataFrame(klines, columns=[
                "time", "open", "close", "high", "low", "volume"
            ])

            df["close"] = df["close"].astype(float)
            df["high"] = df["high"].astype(float)
            df["low"] = df["low"].astype(float)

            return df.tail(60)

        except Exception as e:
            print("data error:", e)
            return None
