from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import databases
import sqlalchemy

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

#database = databases.Database(DATABASE_URL)

#metadata = sqlalchemy.MetaData()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()