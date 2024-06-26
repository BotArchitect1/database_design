from sqlalchemy import Column, Integer, String
from src.db.database import Base


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name})"
