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

def creation_database(cursor):
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

def insert_trainers(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Trainers] (trainer_id, trainer_name)" \
                f"values('{row['trainer_id']}',\"{row['trainer_name']}\")"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_courses(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Courses] (course_id, course_name)" \
                f"values('{row['course_id']}','{row['course_name']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_students(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Students] (student_id,student_name,trainer_id,course_id)" \
                f"values('{row['student_id']}',\"{row['student_name']}\",'{row['trainer_id']}','{row['course_id']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_applicants(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Applicants] (applicant_id,applicant_name,dates,self_development, geo_flex,financial_support, result, course_interest)" \
                f"values('{row['applicant_id']}',\"{row['name']}\",'{row['date']}','{row['self_development']}','{row['geo_flex']}','{row['financial_support_self']}','{row['result']}','{row['course_interest']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_languages(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Languages] (language_id,language_name)" \
                f"values('{row['language_id']}',\"{row['language_name']}\")"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)


def insert_tech_score(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Tech_self_score] (applicant_id,language_id,score)" \
                f"values('{row['applicant_id']}','{row['language_id']}','{row['tech_self_score']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_attributes(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Attributes] (attribute_id,attributes,weaknesses,strengths)" \
                f"values('{row['attribute_id']}',\"{row['attributes']}\",'{row['weaknesses']}','{row['strengths']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)


def insert_junction_table2(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Junction_table2] (applicant_id,attributes_id)" \
                f"values('{row['applicant_id']}','{row['attribute_id']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)

def insert_scores(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Scores] (week_id,student_id,analytics_score,independent_score,determined_score,professional_score,studious_score,imaginative_score)" \
                f"values('{row['Week']}','{row['student_id']}','{row['Analytic']}','{row['Independent']}','{row['Determined']}'," \
                        f"'{row['Professional']}','{row['Studious']}','{row['Imaginative']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)
    query2 = "UPDATE Scores SET \
                analytics_score = NULL, \
                independent_score = NULL, \
                determined_score = NULL, \
                professional_score = NULL,  \
                studious_score = NULL, \
                imaginative_score = NULL \
                WHERE analytics_score = -1;"
    cursor.execute(query2)
                
def insert_junction_table1(df,cursor):
    for index, row in df.iterrows():
        query = f"INSERT INTO [Data32ETL].[dbo].[Junction_table1] (student_id,applicant_id)" \
                f"values('{row['student_id']}','{row['applicant_id']}')"
        cursor.execute("SET QUOTED_IDENTIFIER OFF")
        cursor.execute(query)



   
    
    