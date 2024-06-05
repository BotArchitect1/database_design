from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class BuyBook(Base):
    __tablename__ = "buy_book"

    id = Column(Integer, primary_key=True, index=True)
    buy_id = Column(Integer, ForeignKey("buy.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    buy = relationship("Buy", back_populates="buy_books")
    book = relationship("Book")

    def __repr__(self):
        return f"BuyBook(id={self.id}, buy_id={self.buy_id}, book_id={self.book_id}, quantity={self.quantity})"