from re import DEBUG
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
import sqlalchemy
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@/fastapidemo"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DB_User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(50))
    sex = Column(Boolean, default=True)
    email = Column(String(50))


Base.metadata.create_all(engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
