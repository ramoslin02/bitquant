from enum import Enum

class Exchange(Enum):
    BINANCE = "BINANCE"
    OKEX = "OKEX"
    HUOBI = "HUOBI"
    BYBIT = "BYBIT"

class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP = "STOP"
    FAK = "FAK"
    FOK = "FOK"

class OrderStatus(Enum):
    """
    the order status
    """
    SUBMITTING = "SUBMITTING"  # 提交中
    NOTTRADED = "NOTTRADED"  # 未成交
    PARTIAL = "PARTIAL" # 部分成交
    ALLTRADED = "ALLTRADED"  # 完全成交
    CANCELLED = "CANCELLED"  # 取消订单
    REJECTED = "REJECTED"  # 订单被拒绝


class Timeframe(Enum):
    """time frame 时间窗格
    you may use this for kline.
    """
    MINUTE = '1m'
    HOUR = "1h"
    DAILY = '1d'
    WEEKLY = '1w'
