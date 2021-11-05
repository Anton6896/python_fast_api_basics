from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
for learn porpose in prod use getenv !!!
"""

# local = {}
# with open('.env') as f:
#     lines = f.readlines()
#     for i in lines:
#         key, value = i.split('=')
#         local[key] = value[:-1]


# engine = create_async_engine(
#     f"postgresql+asyncpg://{local.get('USER')}:{local.get('PASSWORD')}@ \
#     {local.get('HOST')}/{local.get('DATABASE')}?prepared_statement_cache_size=100"
# )


SQLALCHEMY_DATABASE_URL = "sqlite:///./blog1.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    except Exception:
        pass
    finally:
        db_session.close()