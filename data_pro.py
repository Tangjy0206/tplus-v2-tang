import requests
import pandas as pd

class DataEnginePro:

    def format_symbol(self, symbol: str):

        symbol = symbol.strip()

        # 自动补交易所（关键修复）
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

            # 🧠 防空结构（关键）
            if not data or "data" not in data:
                return None

            stock_data = data["data"].get(symbol, {})
            klines = stock_data.get("day", [])

            # 🧨 核心防崩点
            if len(klines) == 0:
                return None

            df = pd.DataFrame(klines, columns=[
                "time", "open", "close", "high", "low", "volume"
            ])

            # 强制类型转换（避免字符串）
            df["close"] = pd.to_numeric(df["close"], errors="coerce")
            df["high"] = pd.to_numeric(df["high"], errors="coerce")
            df["low"] = pd.to_numeric(df["low"], errors="coerce")

            df = df.dropna()

            return df.tail(60)

        except Exception as e:
            print("DATA ERROR:", e)
            return None
