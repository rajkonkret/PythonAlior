import teradatasql
import json

db_config = {
    "host": "testzadania-5mr41cxxk0szd7zk.env.clearscape.teradata.com",
    "user": "demo_user",
    "password": "raj12345"
}

try:
    with teradatasql.connect(json.dumps(db_config)) as conn:
        print("Pomyślnie połaczona z Teradata")

        # tworzenie cursora
        with conn.cursor() as cursor:
            query = "SELECT DATE;"
            cursor.execute(query)

            result = cursor.fetchone()  # pobrannie jedego wyniku

            print(result)
except teradatasql.Error as e:
    print("Bład:", e)
# Pomyślnie połaczona z Teradata
# [datetime.date(2025, 11, 20)]

import teradata as td
uda_exec = td.UdaExec(appName='HD', version='1.0', logConsole=False, logLevel='INFO')
# con = uda_exec.connect(method='odbc', dsn='HD', USEREGIONALSETTINGS='N')
with uda_exec.connect(method='odbc', dsn='HD', USEREGIONALSETTINGS='N') as conn:
    print(conn)
