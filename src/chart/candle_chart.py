import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

from data import *

Base.metadata.create_all(bind=engine)

db = SessionLocal()
queryset = get_candle_minute_by_kst(
    db=db,
    market="KRW-BTC",
    start_kst=datetime.fromisoformat("2023-11-10T00:00:00"),
    end_kst=datetime.fromisoformat("2023-11-12T23:59:59"),
)

df = pd.read_sql(queryset.statement, queryset.session.bind)
db.close()

candle = go.Candlestick(
    x=df['CANDLE_DATE_TIME_KST'],
    open=df['OPENING_PRICE'],
    high=df['HIGH_PRICE'],
    low=df['LOW_PRICE'],
    close=df['TRADE_PRICE'],
)

fig = go.Figure(data=candle)
fig.show()
