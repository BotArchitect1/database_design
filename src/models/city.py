from sqlalchemy import Column, Integer, String, DateTime

from src.db.database import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    delivery_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, delivery_time={self.delivery_time})"