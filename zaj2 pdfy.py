from sqlalchemy import create_engine,inspect,MetaData, Table, text, Connection
engine = create_engine('sqlite:///D:/Users/UL0255407/Desktop/Prog wys poz II/census.sqlite')
inspector = inspect(engine)
table_names = inspector.get_table_names()
#wyswietlanie nazw tabel w bd
print(table_names)

#odczytuje bd i buduje obiekt Tabel
#metadata = MetaData()
#census = Table('census', metadata, autoload_with=engine)
#print(repr(census))

#stmt = text('SELECT state, sex FROM census')
#result_proxy = Connection.execute(stmt)
#results = result_proxy.fetchall()

# Zapytanie o unikalne nazwy stanów
states_query = "SELECT DISTINCT state FROM census"

# Wykonanie zapytania
states_result = engine.execute(states_query)

# Wyświetlenie wyników
for row in states_result:
    print(row[0])
