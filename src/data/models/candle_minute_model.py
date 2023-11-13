from sqlalchemy import Column, Integer, String, Double, DateTime
from .. import Base


class CandleMinute(Base):
    __tablename__ = "CANDLE_MINUTE"

    id = Column(String, primary_key=True, index=True, name="ID")
    candle_acc_trade_price = Column(Double, name="CANDLE_ACC_TRADE_PRICE")
    candle_acc_trade_volume = Column(Double, name="CANDLE_ACC_TRADE_VOLUME")
    candle_date_time_kst = Column(DateTime, name="CANDLE_DATE_TIME_KST", index=True)
    candle_date_time_utc = Column(DateTime, name="CANDLE_DATE_TIME_UTC")
    high_price = Column(Double, name="HIGH_PRICE")
    low_price = Column(Double, name="LOW_PRICE")
    market = Column(String, name="MARKET")
    opening_price = Column(Double, name="OPENING_PRICE")
    timestamp = Column(Integer, name="TIMESTAMP")
    trade_price = Column(Double, name="TRADE_PRICE")
    unit = Column(Integer, name="UNIT")
