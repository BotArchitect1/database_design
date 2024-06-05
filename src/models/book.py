from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    genre = relationship("Genre")
    authors = relationship("BookAuthor", back_populates="book")

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, price={self.price}, quantity_in_stock={self.quantity_in_stock}, genre_id={self.genre_id})"
