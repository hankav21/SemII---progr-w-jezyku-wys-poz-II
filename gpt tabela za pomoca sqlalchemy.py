from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///prosta_baza_danych.db', echo=True)

# Deklarowanie bazowej klasy dla modeli
Base = declarative_base()

# Definicja modelu danych
class Dane(Base):
    __tablename__ = 'dane'

    id = Column(Integer, primary_key=True)
    col1 = Column(String)
    col2 = Column(String)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Wstawianie danych do tabeli
dane1 = Dane(col1='wartosc1', col2='wartosc2')
dane2 = Dane(col1='wartosc3', col2='wartosc4')

session.add(dane1)
session.add(dane2)
session.commit()

# Pobieranie i wyświetlanie danych z tabeli
dane = session.query(Dane).all()
print("Zawartość bazy danych:")
for d in dane:
    print(f"ID: {d.id}, Col1: {d.col1}, Col2: {d.col2}")

inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

import shutil

# Skopiowanie pliku bazy danych
shutil.copyfile('prosta_baza_danych.db', 'dane.sqlite')


# Zamykanie sesji
session.close()
