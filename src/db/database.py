from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import config

DATABASE_URL = (
    f"postgresql://{config.db.user}:{config.db.password}"
    f"@{config.db.host}:{config.db.port}/{config.db.name}"
)

Base = declarative_base()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
