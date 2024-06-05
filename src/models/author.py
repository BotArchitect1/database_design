from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.database import Base


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship("BookAuthor", back_populates="author")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"
