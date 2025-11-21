import pandas as pd
from sqlalchemy import create_engine
import os
# pip install teradatasqlalchemy

# pip install sqlalchemy teradatasqlalchemy
# --- KONFIGURACJA ---
# Zastąp swoimi danymi logowania
db_user = "twoj_uzytkownik"
db_password = "twoje_haslo"
db_host = "twoj_host_teradata"

db_config = {
    "host": "testzadania-5mr41cxxk0szd7zk.env.clearscape.teradata.com",
    "user": "demo_user",
    "password": "raj12345"
}
db_user = db_config['user']
db_password = db_config['password']
db_host = db_config['host']
# Nazwa bazy danych i tabeli, z której pobierasz dane
database_name = "DEMO_USER"  # Używam nazwy z Twojego logu
table_name = "Tabela1"

# --- KOD ---
try:
    # Tworzenie "silnika" połączenia za pomocą SQLAlchemy
    # To jest standardowy format URI dla teradatasqlalchemy
    connection_uri = f"teradatasql://{db_user}:{db_password}@{db_host}"

    print("Tworzenie silnika SQLAlchemy...")
    engine = create_engine(connection_uri)

    # Zapytanie SQL
    query = f"SELECT * FROM {database_name}.{table_name};"

    print(f"Pomyślnie utworzono silnik. Pobieranie danych z tabeli: '{database_name}.{table_name}'...")

    # Używamy silnika (engine) bezpośrednio w pd.read_sql().
    # Pandas "rozumie" ten obiekt i nie wyświetli ostrzeżenia.
    # SQLAlchemy automatycznie otworzy i zamknie połączenie.
    df = pd.read_sql(query, engine)

    print(f"\nPobrano {len(df)} wierszy i {len(df.columns)} kolumn.")

    # Wyświetlanie wyników
    if not df.empty:
        print("\n--- Próbka pobranych danych (pierwsze 15 wierszy) ---")
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        print(df.head(15))
    else:
        print("\nTabela jest pusta lub zapytanie nie zwróciło wyników.")

except ImportError:
    print("Upewnij się, że masz zainstalowane biblioteki: pandas, sqlalchemy, teradatasqlalchemy")
except Exception as e:
    print(f"\nWystąpił nieoczekiwany błąd: {e}")

print("\nSkrypt zakończył działanie.")
