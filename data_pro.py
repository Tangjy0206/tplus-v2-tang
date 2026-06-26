import requests
import pandas as pd

class DataEnginePro:

    def get_daily(self, symbol):

        # 腾讯股票接口（稳定）
        url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={symbol},day,,,320,qfq"

        try:
            res = requests.get(url, timeout=10)
            data = res.json()

            klines = data["data"][symbol]["day"]

            df = pd.DataFrame(klines, columns=[
                "time", "open", "close", "high", "low", "volume"
            ])

            df["close"] = df["close"].astype(float)
            df["high"] = df["high"].astype(float)
            df["low"] = df["low"].astype(float)

            return df.tail(60)

        except Exception as e:
            return None
