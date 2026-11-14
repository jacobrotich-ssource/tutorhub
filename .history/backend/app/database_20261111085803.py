import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

database_url = os.environ["DATABASE_URL"]

engine = create_engine(
    database_url,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 3},
)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    with SessionLocal() as session:
        yield session