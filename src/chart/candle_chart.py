import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

from data import *
from utils import db_data_to_candle

Base.metadata.create_all(bind=engine)

db = SessionLocal()
queryset = get_candle_minute_by_kst(
    db=db,
    market="KRW-BTC",
    unit=1,
    start_kst=datetime.fromisoformat("2023-11-10T00:00:00"),
    end_kst=datetime.fromisoformat("2023-11-12T23:59:59"),
)

df = pd.read_sql(queryset.statement, queryset.session.bind)
db.close()
df = db_data_to_candle(df)

candle = go.Candlestick(
    x=df['CANDLE_DATE_TIME_KST'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
)

fig = go.Figure(data=candle)
fig.show()
