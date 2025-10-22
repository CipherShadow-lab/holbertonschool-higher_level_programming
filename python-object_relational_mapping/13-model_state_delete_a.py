#!/usr/bin/python3
"""Script deletes all 'States' objects containing the letter 'a' from database 'hbtn_0e_6_usa'."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    """Access to database to delete State objects with 'a'"""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]),
            pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_del = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_del:
        session.delete(state)
        session.commit()
        session.close()
