def t_signal(df):

    close = df["收盘"]
    high = df["最高"]
    low = df["最低"]

    price = close.iloc[-1]

    ma5 = close.rolling(5).mean().iloc[-1]
    ma10 = close.rolling(10).mean().iloc[-1]

    # 区间位置（核心做T逻辑）
    position = (price - low.min()) / (high.max() - low.min() + 1e-9)

    # ===== 信号系统 =====
    if position < 0.3 and ma5 > ma10:
        return "🟢 低吸做T（机会区）"

    elif position > 0.7:
        return "🔴 高抛区（减仓）"

    elif ma5 > ma10:
        return "🟡 上升趋势（回踩低吸）"

    else:
        return "⚪ 震荡区（观望）"
