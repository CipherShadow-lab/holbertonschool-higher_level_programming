#!/usr/bin/python3
"""Script lists all 'State' objects from database 'hbtn_0e_6_usa'."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ = "__main__":
    """Access to database to get 'states' from database"""

engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
)


Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")
