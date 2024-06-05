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
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    genre = relationship("Genre")
    author = relationship("Author", back_populates="books")
