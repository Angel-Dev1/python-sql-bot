import pyodbc

def connect_to_db(server, database, username, password):
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as e:
        raise Exception(f"Error connecting to database: {e}")

def fetch_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in data]
    except Exception as e:
        raise Exception(f"Error fetching data: {e}")