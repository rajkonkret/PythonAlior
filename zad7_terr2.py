import teradatasql
import json

# --- KONFIGURACJA ---
# Zastąp swoimi danymi logowania
# db_config = {
#     "host": "twoj_host_teradata",
#     "user": "twoj_uzytkownik",
#     "password": "twoje_haslo"
# }
db_config = {
    "host": "testzadania-5mr41cxxk0szd7zk.env.clearscape.teradata.com",
    "user": "demo_user",
    "password": "raj12345"
}
# Nazwa bazy danych i tabeli, którą chcesz utworzyć
database_name = "DEMO_USER"
table_name = "Tabela2"

# --- POPRAWIONY SKRYPT SQL DO UTWORZENIA TABELI ---
# Używamy składni "UNIQUE PRIMARY INDEX (UPI)" specyficznej dla Teradata
create_table_sql = f"""
CREATE TABLE {database_name}.{table_name} (
    ID INTEGER NOT NULL,
    Nazwa VARCHAR(100) CHARACTER SET UNICODE,
    Wartosc DECIMAL(10, 2)
)
UNIQUE PRIMARY INDEX (ID);
"""

# --- KOD WYKONAWCZY ---
try:
    # Nawiązywanie połączenia z bazą danych
    with teradatasql.connect(json.dumps(db_config)) as conn:
        print("Pomyślnie połączono z Teradata.")

        # Tworzenie obiektu kursora
        with conn.cursor() as cursor:
            print(f"Próba utworzenia tabeli: {database_name}.{table_name}")

            try:
                # Wykonanie polecenia CREATE TABLE
                cursor.execute(create_table_sql)
                print("Tabela została pomyślnie utworzona!")
            except teradatasql.Error as e:
                # Sprawdzenie, czy błąd dotyczy już istniejącego obiektu (kod błędu 3807)
                if "3807" in str(e):
                    print(f"Tabela '{table_name}' już istnieje w bazie danych. Nie wykonano żadnych zmian.")
                else:
                    # Rzucenie błędu dalej, jeśli jest to inny problem
                    raise e

except teradatasql.Error as e:
    print(f"Wystąpił błąd podczas operacji na bazie danych: {e}")
except ImportError:
    print("Biblioteka 'teradatasql' nie jest zainstalowana. Użyj 'pip install teradatasql'.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")

print("\nSkrypt zakończył działanie.")
