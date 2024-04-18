from sqlalchemy import create_engine, inspect, func, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///D:/Users/UL0255407/Desktop/Prog wys poz II/census.sqlite')

inspector = inspect(engine)
columns = inspector.get_columns('census')

# Wyświetlenie nazw i typów kolumn
print("Kolumny w tabeli census:")
for column in columns:
    print(f"Nazwa: {column['name']}, Typ: {column['type']}")

Base = declarative_base()

# Definicja modelu danych
class Census(Base):
    __tablename__ = 'census'

    id = Column(Integer, primary_key=True)
    state = Column(String)
    sex = Column(String)
    age = Column(Integer)
    pop2000 = Column(Integer)  # Kolumna z danymi o populacji w 2000 roku
    pop2008 = Column(Integer)  # Kolumna z danymi o populacji w 2008 roku

# Utworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Polecenie 1: Nazwy stanów występujące w bazie
states = session.query(Census.state).distinct().all()
print("Nazwy stanów występujące w bazie:")
for state in states:
    print(state[0])

# Polecenie 2: Policz populacje w stanie Alaska oraz New York w 2000 oraz 2008 roku
populations = session.query(func.sum(Census.pop2000), func.sum(Census.pop2008)).filter(Census.state.in_(['Alaska', 'New York'])).all()
print("\nPoliczona populacja w stanie Alaska oraz New York w 2000 oraz 2008 roku:")
for result in populations:
    print(f"Populacja w 2000 roku: {result[0]}, Populacja w 2008 roku: {result[1]}")

# Polecenie 3: Policz liczbę kobiet oraz mężczyzn w stanie New York w 2008 roku
gender_counts = session.query(Census.sex, func.sum(Census.pop2008)).filter(Census.state == 'New York').group_by(Census.sex).all()
print("\nPoliczona liczba kobiet oraz mężczyzn w stanie New York w 2008 roku:")
for gender_count in gender_counts:
    print(f"Płeć: {gender_count[0]}, Liczba osób: {gender_count[1]}")

# Zamykanie sesji
session.close()