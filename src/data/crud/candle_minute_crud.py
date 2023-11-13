from datetime import datetime
from sqlalchemy.orm import Session

from ..models import CandleMinute


def get_all_candle_minute(db: Session, market: str):
    return db.query(CandleMinute).filter(CandleMinute.market == market)


def get_candle_minute_by_kst(db: Session, market: str, start_kst: datetime, end_kst: datetime):
    return db.query(CandleMinute).filter(CandleMinute.market == market).filter(CandleMinute.candle_date_time_kst >= start_kst).filter(CandleMinute.candle_date_time_kst <= end_kst)
