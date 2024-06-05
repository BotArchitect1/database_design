from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class Buy(Base):
    __tablename__ = "buy"

    id = Column(Integer, primary_key=True, index=True)
    wishes = Column(String, nullable=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    client = relationship("Client")
    buy_books = relationship("BuyBook", back_populates="buy")
