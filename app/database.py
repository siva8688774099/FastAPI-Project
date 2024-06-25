from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from config import db_creds


DATABASE_URL = f"postgresql+psycopg2://{db_creds.db_user}:{db_creds.db_password}@{db_creds.db_host}/{db_creds.db_name}"

engine = create_engine(DATABASE_URL, pool_size=30, max_overflow=50)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
