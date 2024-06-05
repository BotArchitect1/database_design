from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class BookAuthor(Base):
    __tablename__ = "book_author"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"BookAuthor(id={self.id}, book_id={self.book_id}, author_id={self.author_id})"