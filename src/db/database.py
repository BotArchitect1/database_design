from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL

from src.config import config

DATABASE_URL: URL = URL.create(
    drivername="postgresql",
    username=config.db.user,
    password=config.db.password,
    host=config.db.host,
    port=config.db.port,
    database=config.db.name,
)

Base = declarative_base()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db: Session = Session()
    try:
        yield db
    finally:
        db.close()
