import akshare as ak

class DataEngine:

    def get_daily(self, symbol):
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period="daily",
            adjust="qfq"
        )
        return df.tail(60)

    def get_min(self, symbol, period="5"):
        try:
            df = ak.stock_zh_a_hist_min_em(
                symbol=symbol,
                period=period,
                adjust="qfq"
            )
            return df.tail(100)
        except:
            return None
