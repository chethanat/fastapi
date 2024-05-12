from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings

SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
print("DATABASE URL is", SQLALCHEMY_DATABASE_URL)

# engine is the entry point for any SQL alchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autoflash=False, autocommit=False, bind=engine)