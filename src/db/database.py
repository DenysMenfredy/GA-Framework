from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from sqlalchemy import text

PATH = dotenv_values('./.env')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{PATH['DB_USER']}:{PATH['DB_PASSWORD']}@{PATH['DB_HOST']}:{PATH['DB_PORT']}/{PATH['DB_NAME']}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

with engine.connect() as con:
    result = con.execute('SELECT 1+1')
    print(result.fetchone())
    

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

