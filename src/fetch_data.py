import mysql.connector
import json

def fetch_data_from_mysql(server, user, password, database, table_name):
    con = None
    cursor = None
    try:
        con = mysql.connector.connect(
            host=server,
            user=user,
            password=password,
            database=database,
            port=3306
        )
        cursor = con.cursor()
        
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        
        json_data = json.dumps([dict(zip(columns, row)) for row in data], default=str)
        
        return json_data
    except mysql.connector.Error as e:
        return json.dumps({"error": str(e)})
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

if __name__ == "__main__":
    server = '127.0.0.1'
    user = 'root'
    password = 'aryan7669'
    database = 'ORG'
    table_name = 'TITLE'

    json_data = fetch_data_from_mysql(server, user, password, database, table_name)
    print(json_data)
