# рассмотрим пример создания реальной бд с таблицами
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

DB_URL = "sqlite:///./sql_db.db"

# создаем движок sqlalchemy
engine = create_engine(
    DB_URL, connect_args={"check_same_thread" : False}
)

# Для создания базы данных и таблиц по метаданным моделей применяется метод Base.metadata.create_all().
# Его ключевой параметр - bind принимает класс, который используется для подключения к базе данных.
# В качестве такого класса применяется созданный ранее движок SQLAlchemy.
# Если база данных и все необходимые таблицы уже имеются, то метод не создает заново таблицы.


# создаем базовый класс для моделей
class Base(DeclarativeBase): pass

# создаем модель, объекты которой будут хранитсья в бд
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# создаем таблицы
Base.metadata.create_all(bind = engine)

app = FastAPI()

