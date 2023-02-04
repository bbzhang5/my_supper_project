from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import pymysql
pymysql.install_as_MySQLdb()


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:zbb123456@localhost:3306/pestogreenzbb'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Each instance of the SessionLocal class will be a database session.

Base = declarative_base()
# we will inherit from this class to create each of the database models or classes (the ORM models)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()