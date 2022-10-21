'''from turtle import title
import rec as rec
from lxml.html.defs import tags
from numpy import record
from pymongo import MongoClient
from scripts.regsetup import description
try:

    client = MongoClient("mongodb://localhost:27017")
    print("Connexion au client reussie")

    try:
        db = client.basebot
        print("Connexion a la bd")
    except:
        print("connexion a la bd echouee")
    try:
        product = db.product
        print("Connexion a la collection product")
    except:
        print("connexion a la bd echouee")
    try:
        Clients = db.clients
        Commandes=db.commandes
        print("Connexion a la collection client")
    except:
        print("connexion a la bd echouee")

except :
    print("connexion au client echouee")


Commandes.insert_many([
    {
        "id":'62d',
        "Firstname": "en",
        "LastName": "m",
        "client_age": 78
    },
    {
        "id": '6d53430f81aa04804286b13',
        "Firstname": "Bie",
        "LastName": "ma",
        "client_age": 45
    }
]
)
a = Clients.find_one({"Firstname":"okay"})
print(a)
'''

