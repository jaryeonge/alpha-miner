import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def check_mysql_env() -> str:
    try:
        db_user = os.environ["DB_USERNAME"]
        db_password = os.environ["DB_PASSWORD"]
        db_url = os.environ["DB_URL"]
        db_name = os.environ["DB_NAME"]
        return f"mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}?charset=utf8mb4"
    except KeyError as e:
        logging.error(e)


engine = create_engine(check_mysql_env())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
