import pyodbc



server = '18.135.105.184'

database = 'Northwind'

username = 'SA'

password = 'Passw0rd2018'

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'

                                  'SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()



# cursor.execute("SELECT * FROM Products")

# row = cursor.fetchone()



# for row in cursor.execute("SELECT * FROM Products").fetchall(): # too much information trying to store it in a variable (There is a way down below)

#     print(row.UnitPrice)



rows = cursor.execute("SELECT * FROM Products") # A way around for fetchall too much data problem

while True:

    record = rows.fetchone()

    if record is None:

        break

    print(record.UnitPrice)