import pyodbc


def cursor_creation():
    server = 'localhost,1433'
    database = 'master'
    username = 'SA'
    password = 'Passw0rd2018'
    docker = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
    cursor = docker.cursor()
    return cursor

def create_database(cursor):
    with open("Table_Creator.sql", 'r') as file:
            query = file.read()
    cursor.execute(query)  
    cursor.commit()


def insert_into(cursor, df, table_name, columns):
    for index, row in df.iterrows():
        cursor.execute(f"INSERT INTO academy."+table_name+"("+columns+") values(?,?,?)")

if __name__ == "__main__":
    cursor = cursor_creation()
    create_database(cursor)
    