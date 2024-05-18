from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import MetaData

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

metadata = MetaData()

engine = create_engine(DATABASE_URL, poolclass=NullPool)
session_maker = sessionmaker(engine, autocommit=False, autoflush=False)

def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()