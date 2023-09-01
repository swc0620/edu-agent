import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_DB_URL = os.getenv("MYSQL_DB_URL", "mysql+pymysql://root:root@db/edu-agent")

engine = create_engine(MYSQL_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
