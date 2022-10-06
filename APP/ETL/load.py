import pyodbc
from transform import *

def cursor_creation():
    server = 'localhost,1433'
    database = 'master'
    username = 'SA'
    password = 'Passw0rd2018'
    docker = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
    cursor = docker.cursor()
    return cursor

def creation_database():
    for i in cursor.execute(f"SELECT * FROM sys.databases"):
        database_list = []
        database_list.append(i[0])
    if 'Data32ETL' in database_list:
        cursor.execute("DROP DATABASE IF EXISTS [Data32ETL]")
        cursor.execute("CREATE DATABASE [Data32ETL]")
    else:
        cursor.execute("CREATE DATABASE [Data32ETL]")

def create_tables(cursor):
    with open("Table_Creator.sql", 'r') as file:
            query = file.read()
    cursor.execute(query)
    cursor.commit()


def insert_into(cursor, df, table_name, rows):
    for index, row in df.iterrows():
        cursor.execute(f"INSERT INTO academy.{table_name} VALUES ({rows})")

def insert_trainers(df):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Trainers] (trainer_id, trainer_name)" \
                f"values('{row['trainer_id']}',\"{row['trainer_name']}\")"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_courses(df):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Courses] (course_id, course_name)" \
                f"values('{row['course_id']}','{row['course_name']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_students(df):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Students] (student_id,student_name,trainer_id,course_id)" \
                f"values('{row['student_id']}',\"{row['student_name']}\",'{row['trainer_id']}','{row['course_id']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

if __name__ == "__main__":
    cursor = cursor_creation()
    creation_database()
    create_tables(cursor)
    insert_courses(course_name_table())
    insert_trainers(create_trainers_table())
    insert_students(table_students())
    
   
   
    
    