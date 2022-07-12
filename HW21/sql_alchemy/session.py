from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine('postgresql://sergeymatkobozhyk:123@localhost/postgres')
__session = sessionmaker(engine)

session: Session = __session()


def create_db():
    Base.metadata.create_all(engine)



