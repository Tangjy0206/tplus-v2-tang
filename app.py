import streamlit as st
import akshare as ak

st.set_page_config(page_title="T+做T工具", layout="centered")

st.title("📊 T+盘中做T系统")

symbol = st.text_input("输入股票代码（如 000001）")

if symbol:

    try:
        df = ak.stock_zh_a_hist(symbol=symbol, period="daily", adjust="qfq")

        close = df["收盘"]
        vol = df["成交量"]

        ma5 = close.rolling(5).mean().iloc[-1]
        ma10 = close.rolling(10).mean().iloc[-1]
        price = close.iloc[-1]

        st.write("价格：", price)
        st.write("MA5：", ma5)
        st.write("MA10：", ma10)

        if price > ma5 and vol.iloc[-1] > vol.mean() * 1.5:
            st.success("🟢 LONG（可做T）")
        elif price < ma10:
            st.error("🔴 RISK（不建议操作）")
        else:
            st.warning("🟡 WAIT（观察）")

    except Exception as e:
        st.error("数据加载失败，请稍后再试")
        st.write(e)
