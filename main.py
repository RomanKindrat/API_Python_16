from xmlrpc.client import DateTime
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer, DateTime, BIGINT, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship


labpp = mysql.connector.connect(
  host="localhost",
  user="root",
  database='cinema',
  password="1324qewr"
)


engine = create_engine('mysql+mysqlconnector://root:1324qewr@localhost:3306/cinema', pool_pre_ping=True)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()

class Role(Base):
  __tablename__ = 'Role'

  idRole = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)

class User(Base):
  __tablename__ = 'User'

  idUser = Column(Integer, primary_key=True)
  userName = Column(String(45), unique=True)
  firstName = Column(String(45), nullable=False)
  secondName = Column(String(45), nullable=False)
  email = Column(String(45), unique=True)
  password = Column(String(255), nullable=False)
  phone = Column(String(45), nullable=True)
  id_idRole = Column(Integer, ForeignKey(Role.idRole))
  Role = relationship(Role, backref='User', lazy="joined")

class Category(Base):
  __tablename__ = 'Category'

  idCategory = Column(Integer, primary_key=True)
  category = Column(String(45), nullable=False)

class Hall(Base):
  __tablename__ = 'Hall'

  idHall = Column(Integer, primary_key=True)
  hall_number = Column(Integer, nullable=False)
  capacity = Column(Integer, nullable=False)
  status = Column(String(45), nullable=False)

class Film(Base):
  __tablename__ = 'Film'

  idFilm = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  duration = Column(Integer, nullable=False)
  photo = Column(String(45), nullable=False)
  id_idCategory = Column(Integer, ForeignKey(Category.idCategory))
  Category = relationship(Category, backref='Film', lazy="joined")

class Schedule(Base):
  __tablename__ = 'Schedule'

  idSchedule = Column(Integer, primary_key=True)
  date = Column(DateTime, nullable=False)
  id_idFilm = Column(Integer, ForeignKey(Film.idFilm))
  Film = relationship(Film, backref='Schedule', lazy="joined")
  id_idHall = Column(Integer, ForeignKey(Hall.idHall))
  Hall = relationship(Hall, backref='Schedule', lazy="joined")

class Cinema(Base):
  __tablename__ = 'Cinema'

  idCinema = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  address = Column(String(200), nullable=False)

class JWTTokens(Base):
  __tablename__ = 'JWTTokens'

  idToken = Column(Integer, primary_key=True)
  token = Column(String(300), nullable=False)


# Base.metadata.create_all(engine)
