import pyodbc
# Connexion approuvée à l'instance nommée
import pyodbc


from app import chatbotResponse, sqlquery



import pyodbc
"""""# Connexion approuvée à l'instance nommée
import pyodbc
def connect_database(query_s):
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-LDG1A51;'
                              'Database=echat_database;'
                              'Trusted_Connection=yes;')
        print("sql connexion reussie")
    except:
        print("sql connexion échouée")

    try:
        cursor = conn.cursor()
        a=cursor.execute('SELECT * FROM PRODUCTS')
    except:
        print("connexion query échouée")

    for i in cursor:
        print(i)
    return a"""""