from datetime import datetime
from sqlalchemy.orm import Session

from ..models import CandleMinute


def get_all_candle_minute(db: Session, market: str, unit: int):
    return db.query(CandleMinute).filter(CandleMinute.market == market).filter(CandleMinute.unit == unit)


def get_candle_minute_by_kst(db: Session, market: str, unit:int, start_kst: datetime, end_kst: datetime):
    return db.query(CandleMinute).filter(CandleMinute.market == market).filter(CandleMinute.unit == unit).filter(CandleMinute.candle_date_time_kst >= start_kst).filter(CandleMinute.candle_date_time_kst <= end_kst)
