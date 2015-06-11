from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///foo.db')

meta = MetaData()
company = Table('employee', meta, autoload=True, autoload_with=engine)

print 'printing columns and types'
for c in company.columns:
    print '{} - type {}'.format(c.name, c.type)
