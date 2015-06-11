from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

if __name__ == '__main__':
    # prepare connection
    engine = create_engine('sqlite:///foo.db')
    
    # declare base as being auto-mapping
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    # this will be the db connection session
    session = Session(engine)

    # this is a db object, a table
    # NOTE: case-sensitivity
    employee = Base.classes.EMPLOYEE

    all_employees = session.query(employee).all()

    print 'printing all employee names'
    for emp in all_employees:
        print emp.NAME

    # selecting just one employee
    some_employees = session.query(employee).filter_by(NAME="Paul").all()

    for emp in some_employees:
        print emp.NAME

    # you need to find out the name of the columns
    # and what type of values they accept
    # run the show_columns.py script to see a sample

    # we know the following
    # ID - type INTEGER
    # NAME - type TEXT
    # AGE - type INTEGER
    # ADDRESS - type CHAR(50)
    # SALARY - type REAL

    # tricky part
    # how do we make sure we create a unique ID?
    # let's just get the highest one atm
    # and use the next one!

    # this is a function.
    # it returns the maximum of all entries in the ID column
    # in this table
    last_employee = session.query(func.max(employee.ID).label("next_id")).one()

    NEXT_ID = last_employee.next_id + 1

    print 'creating new employee with id {}'.format(NEXT_ID)
    # You still need to know the column names to create a new user
    # But look, ma, no SQL!
    new_emp = employee(
        ID=NEXT_ID,
        NAME="Jack",
        AGE=33,
        ADDRESS="30 Rock",
        SALARY="2000")
    session.add(new_emp)
    session.commit()

    # testing to see if the new user is there
    some_employees = session.query(employee).filter_by(NAME="Jack").all()

    print 'the new employee is here'
    for emp in some_employees:
        print emp.NAME

