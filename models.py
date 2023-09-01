from sqlalchemy import Column, Integer, TEXT
from db import Base


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True, index=True)
    summary = Column(TEXT)
