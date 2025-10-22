#!/usr/bin/python3
"""
Script deletes all 'States' objects containing the letter 'a'
from database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from mode_city import City
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

    query = session.query(City, State).join(State)

    for city, state in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
