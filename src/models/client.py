from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)

    city = relationship("City")

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, email={self.email}, city_id={self.city_id})"