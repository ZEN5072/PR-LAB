from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://todo:todo@db-lab3:5432/todo_db" 
# "postgresql://<username>:<password>@<host>:<port>/<database_name>"
# Харчевно, но это не важно... (хард код сИла, АУФ)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
