import pandas as pd
from datetime import datetime
from typing import Type
from backtesting import Backtest, Strategy

from data import *
from utils import constants, db_data_to_candle
from strategies.base_strategy import SmaCross

Base.metadata.create_all(bind=engine)


def backtest_strategy(
        strategy: Type[Strategy],
        market: str,
        start_kst: datetime,
        end_kst: datetime,
        unit: int,
        cash: int = constants.DEFAULT_TEST_CASH,
        commission: float = constants.UPBIT_KRW_COMMISSION
) -> Backtest:
    db = SessionLocal()
    queryset = get_candle_minute_by_kst(db=db, market=market, unit=unit, start_kst=start_kst, end_kst=end_kst)
    df = pd.read_sql(queryset.statement, queryset.session.bind)
    db.close()

    df = db_data_to_candle(df)
    return Backtest(df, strategy, cash=cash, commission=commission, exclusive_orders=True)


# example
bt = backtest_strategy(SmaCross, "KRW-BTC", datetime.fromisoformat("2023-01-01T00:00:00"), datetime.fromisoformat("2023-12-31T23:59:59"), 60)

output = bt.run()
output.get("Return [%]")
bt.plot()

stats, heatmap = bt.optimize(
    n1=range(10, 150, 10),
    n2=range(30, 250, 10),
    constraint=lambda p: p.n1 < p.n2,
    maximize="Equity Final [$]",
    return_heatmap=True
)

print(heatmap.sort_values().iloc[-3:])



