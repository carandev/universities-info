from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/universities_info_db"

db_engine = create_engine(DATABASE_URL)

connection = db_engine.connect()

meta = MetaData()

Base = declarative_base(db_engine)
