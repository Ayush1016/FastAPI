from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/bookstore"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    base.metadata.create_all(engine)
    