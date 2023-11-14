import pandas as pd


def db_data_to_candle(df: pd.DataFrame) -> pd.DataFrame:
    mapper = {
        "OPENING_PRICE": "Open",
        "HIGH_PRICE": "High",
        "LOW_PRICE": "Low",
        "TRADE_PRICE": "Close",
    }

    new_df = df.rename(columns=mapper, errors="raise")
    new_df = new_df.set_index(df["CANDLE_DATE_TIME_KST"])
    return new_df
