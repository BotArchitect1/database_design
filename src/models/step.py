from sqlalchemy import Column, Integer, String

from src.db.database import Base


class Step(Base):
    __tablename__ = "step"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
