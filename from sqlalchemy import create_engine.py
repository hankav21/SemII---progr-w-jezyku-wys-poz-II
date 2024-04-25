import sqlite3

# Funkcja do tworzenia tabeli i wstawiania danych
def create_database():
    # Połączenie z bazą danych (tworzy bazę danych, jeśli nie istnieje)
    conn = sqlite3.connect('prosta_baza_danych.db')
    c = conn.cursor()

    # Tworzenie tabeli
    c.execute('''CREATE TABLE IF NOT EXISTS dane
                 (id INTEGER PRIMARY KEY, col1 TEXT, col2 TEXT)''')

    # Wstawianie danych do tabeli
    c.execute("INSERT INTO dane (col1, col2) VALUES ('wartosc1', 'wartosc2')")
    c.execute("INSERT INTO dane (col1, col2) VALUES ('wartosc3', 'wartosc4')")

    # Zapisanie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()

# Funkcja do wyświetlania zawartości tabeli
def display_database():
    # Połączenie z bazą danych
    conn = sqlite3.connect('prosta_baza_danych.db')
    c = conn.cursor()

    # Wykonanie zapytania SQL
    c.execute("SELECT * FROM dane")

    # Pobranie wyników zapytania
    rows = c.fetchall()

    # Wyświetlenie wyników
    for row in rows:
        print(row)

    # Zamknięcie połączenia
    conn.close()

# Tworzenie bazy danych
create_database()

# Wyświetlanie zawartości bazy danych
print("Zawartość bazy danych:")
display_database()
