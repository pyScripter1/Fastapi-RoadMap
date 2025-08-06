# Создание сессии данных

# Для взаимодействия с базой данных необходимо создать сессию базы данных,
# которая представляет объект sqlalchemy.orm.Session. Через этот объект идет вся работа с БД.
# Но для этого вначале надо создать класс-построитель Session с помощью функции-фабрики sessionmaker()

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )

# создаем таблицы
Base.metadata.create_all(bind = engine)

# autoflush = True - автоматически записываем все изменения в бд
# bind = engine - подключение к движку
# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=True, bind=engine)
# так как это класс, создаем объект нашего класса
db = SessionLocal() # объект Session

# создаем объект для добавления в бд
person1 = Person(name="Daniil", age=54)
db.add(person1) # добавляем в бд
person2 = Person(name="Alice", age=33)
person3 = Person(name="Alex", age=43)
db.add_all([person2, person3])
db.commit() # сохраняем изменения


# Для получения объектов из базы данных вначале у объекта
# Session необходимо вызывать метод query() - в него передается тип модели, данные которой необходимо получить:
people = db.query(Person).all() # метод all для получения всех объектов
for person in people:
    print(f"{person.id}. {person.name} - {person.age}")

# для получения одного объекта, можно использовать метод get(), туда указываем тип модели и id
one_person = db.get(Person, 2)
print(one_person.id, one_person.name, one_person.age)

# для фильтрации у объекта Query есть метод filter, который принимает условие фильтрации
result_person = db.query(Person).filter(Person.age > 40).all()
for p in result_person:
    print(p.name)

# удаления объекта (записи в таблице)
db.delete(person1)
db.commit()