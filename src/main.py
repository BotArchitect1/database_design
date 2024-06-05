from src.db.database import Base, engine
from src.models import author, book, buy, buy_book, buy_step, city, client, genre, step


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
