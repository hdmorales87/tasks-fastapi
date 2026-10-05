from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres",
    port=5432
)

engine = create_engine(url)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()


def get_db():
    db = Session()

    try:
        yield db
    finally:
        db.close()