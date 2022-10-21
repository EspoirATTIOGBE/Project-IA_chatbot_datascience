from idlelib import query
from urllib import response

import pyodbc
# Connexion approuvée à l'instance nommée
import pyodbc
import requests
import translator as translator
from Demos.getfilever import lang
from jupyterlab_widgets import data
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, g
from googletrans import Translator
import os
import googletrans
from googletrans import Translator
from langdetect import detect
import openai
from tensorflow.python.framework.test_ops import none


#Clé d'api openai
openai.api_key = "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"
import processor
import chatgui

from googletrans import Translator

app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

#La route concernant l'interface web(mainbot.html)
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('mainbot.html', **locals())


#La route concernant les différentes fonctionnalités et des réponses du chatbot
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        #Récuperation des entrées de l'utilisateur
        the_question = request.form['messageValue']
        #value = Commandes.find_one({"id":the_question})
        #print(value)
        #dectection puis traduction de réponse en langue d'entré de l'utilisateur
        translator = Translator()
        detector=translator.detect(the_question)
        detection_language=detector.lang
        #Affichage de la langue détectée
        print(detection_language)
        #Traduction de la langue détectée en langue du model(Anglais)
        translation = translator.translate(the_question,dest="en")
        print(the_question)
        #Affichage du sentiment de la phrase  à l'aide de la méthode Sentiment()
        senti = sentiment(translation.text)
        print(senti)
        print(translation.text)
        print(the_question)
        #Générateur de requete en fonction de la phrase de l'utilisateur en utilisant la méthode query_sentence()
        query_sentence=sqlquery(translation.text)
        #print(query_sentence)
        #Reponse traduite dans la langue d'entrée de l'utilisateur
        conv = conversation(translation.text)
        translation_to_detect_conv = translator.translate(conv, dest=detection_language)
        print(translation_to_detect_conv.text)
        conv_translate = translation_to_detect_conv.text
        print(conv)
        #c=connect_database(query_sentence)
        #print(c)
        #print(query_sentence)
        #Retour de la réponse du bot(Agent Espoir) en fonction de la requête trouvée ou définie
        g=return_response(query_sentence)
        d=final_conversation(query_sentence,conv_translate,g)
        #response = chatgui.chatbot_response(the_question)
    return jsonify({"response": d,"sentiment": senti,"query":query_sentence})

'''Cette fonction permet au bot de savoir après toutes les déductions, ce qu'il va définir comme réponse en fonction de la requête
trouvée.
-Si requête trouvée= Not query, alors la question ne nécissite pas une requête vers une base..Ce qui permet au bot de savoir que
c'est une question ordinaire  et la réponse à donner est juste tiré de son intelligence.
-Si la requête trouvée != Not query , alors la question génère une requête vers une base..Ce qui indique au bot de rechercher
des infomations avant de donner une réponse '''
def final_conversation(query_sentence,conv_translate,g):

    if(query_sentence=='Not query'):
        return conv_translate
    elif (query_sentence!= 'Not query'):
        return g
#Fonction qui indique une conversation normale et la création en tant qu'humain du bot(Agent Espoir)
def conversation(text):
    prompt = discut+text+"\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\nHuman:", " AI:"])
    return response["choices"][0]["text"]
    # return jsonify({"response":"OK"})
#Fonction qui permet la géneration des requêtes
def sqlquery(text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="#Table Category, columns=[CategoryId,CategoryName]\\n#Table Products, columns=[ProductId,ProductName , ProductDescription,UnitPrice, UnitsinStock,CategoryId]\\\n#Table Payment,  columns=[PaymentId,Payement_Method,Payment_Amount,Payment_State]\\n#Table Customer, columns=[CustomerId,FirstName , City,Tel]\n#Table Orders, columns=[OrderId,OrderNumber,OrderStatus,RequiredDate,PaymentDate,OrderDate,CustomerId,PaymentId]\n#Table OrdersDetails, columns=[OrderDetailId, OrderNumber,Quantity,Price,OrderId,ProductId]\n# R language SQL\n\nCreate SQL query  for sentence of e-commerce\nHello,how are you?\nNot query\nwhat about your day?\nNot query\ni want to know products that you have?\nSELECT ProductName\nFROM Products\nThe product in Produit are: \n\ni  want to know the price of the techno camon 11?\nSELECT UnitPrice\nFROM Products\nWHERE ProductName = 'techno camon 11'\nwhat is the price of the product?\nNot query\niphone 10\nSELECT UnitPrice\nFROM Products\nWHERE ProductName = 'iphone 10'\nokay thank!\nNot query \ni want to know  the price of his product?\nNot query\nthe name of product is iphone 18\nSELECT UnitPrice\nFROM Products\nWHERE ProductName = 'iphone 18'\nwhat are the products and their categories that you have?\nSELECT ProductName, CategoryName\nFROM Products\nJOIN Category\nON Products.CategoryId = Category.CategoryId\nwhat is the status of my order please?\nnot query\nmy order number is 451geNHGJE\nSELECT OrderStatus\nFROM Orders\nWHERE OrderNumber = '451geNHGJE'\nokay thanks!\nNot query\nwhat is the amount of the payment related to my order please?\nnot query\nmy OrderNumber is 451geNHGJE\nSELECT Payment_Amount\nFROM Payment\nJOIN Orders\nON Payment.PaymentId = Orders.PaymentId\nWHERE Orders.OrderNumber = '451geNHGJE'\nokay !\nNot query\ni want to know products that you have?\nSELECT ProductName\nFROM Products\nThe product in Produit are:\n\nokay cool!\ni want to know products that you have?\nSELECT ProductName\nFROM Products\nThe product in Produit are: \n\nokay !\nNot query😅\nNot query\nBonjour,je vous espère bien.J'ai fais un sondage sur votre site web et j'ai su que vous vendez des produits..Puis-je savoir ceux que vous avez svp?\nSELECT ProductName\nFROM Products\nThe product in Produit are:\nokay thanks!\nNot query\n"+text+"\n",
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]


'''def translate(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = "q="+text+"&target=fr&source=en"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "f3fafe3e5amsha8e426210097fb7p17cd2ajsne4e7bb3b91b7",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
'''
#Fonction qui permet de déterminer le sentiment de la phrase entrée par l'utilisateur
def sentiment(text):
    prompt = "This is a Sentence classifier\n\n\nSentence: \"I loved the new Batman movie!\"\nSentiment: Positive\n###\nSentence: \"I hate it when my phone battery dies.\"\nSentiment: Negative\n###\nSentence: \"My day has been 👍\"\nSentiment: Positive\n###\nSentence: \"This is the link to the article\"\nSentiment: Neutral\n###\nSentence: "+text+"\nSentiment:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["###"])
    return response["choices"][0]["text"]
    # return jsonify({"response":"OK"})

'''try:

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
        print("Connexion a la collection client")
        Commandes = db.commandes
    except:
        print("connexion a la bd echouee")

except :
    print("connexion au client echouee")!!!
'''

#La fonction qui permet de fomuler ou de retourner une réponse suite aux résultats des différentes requêtes trouvées
def return_response(query_sentence):
    if(query_sentence!='Not query'):
        response = openai.Completion.create(
                model="text-davinci-002",
                prompt="#Table Category, colums=[CategoryId,CategoryName]\n#Table Products, columns=[ProductId,ProductName , ProductDescription,UnitPrice, UnitsinStock,CategoryId]\n#Table Payment,  columns=[PaymentId,Payement_Method,Payment_Amount,Payment_State]\n#Table Customer, columns=[CustomerId,FirstName , City,Tel]\n#Table Orders, columns=[OrderId,OrderNumber,OrderStatus,RequiredDate,PaymentDate,OrderDate,CustomerId,PaymentId]\n#Table OrdersDetails, columns=[OrderDetailId, OrderNumber,Quantity,Price,OrderId,ProductId]\n#Table Delivery, columns=[DeliveryId,Adress_delivery,Delivery_Date,OrderNumber,OrderId]\n# R language SQL \n#Values=(1, 'Iphone17','Phone de qualité premium', '300000', 10,49),(3, 'Iphone 12','Très original et efficace', '1000000', 0,45),(4, 'Camon','Très', '9000000', 0,65)]\n\nit is a showing result of sql query \nThis is first example of response of the  query:\nSELECT UnitPrice FROM Products WHERE ProductName='Camon'\n\nAvec nous, le prix de Camon n'est pas excessif . Il vaut  9000000 FCFA\nThis is second example of response of the  query \n\nSELECT UnitPrice\nFROM Products\nWHERE ProductName='iphone 12','techno 10'\n\nPar rapport à votre demande, nous disposons que de l'iphone 12 et non le techno 10..Son prix est 1000000 FCFA\n\nThis is third example of response of the  query \nSELECT ProductName FROM Products \nWe have product like:\n\nCher client, nous vendons des produits de qualité  qui sont:\n-Iphone 17,\n-phone 12\n-Camon\n\nProduit= [(1, 'Samsung S5','Phone de qualité premium', '800000', 10,49),(2, 'techno spark 4','Très original et efficace', '750000', 0,45)(3, 'Iphone x','Nouvelle gamme de produit très puissant', '5000000', 52,165),(4, 'Iphone Xr','Produit énormément commandé et valorisé', '2000000', 52,165),(5, 'Huawei','Nouveauté avec une caméra claire', '19000000', 52,165)]\n \nit is a showing result as sentence for queries  by using  data in Produit and the   first and second example of response .Return ''Veuillez-nous excusez cher client,  nous n'avons pas ce produit'' if the product is not in Produit.\n"+query_sentence+"\n",
                temperature=0,
                max_tokens=60,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        return response["choices"][0]["text"]
    elif(query_sentence== 'Not query'):
        return 0
# Connexion approuvée à l'instance nommée de la base de données (Pas nécessaire si le projet est spécifique pour une entreprise)
import pyodbc
def connect_database(query_sentence):
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-LDG1A51;'
                              'Database=echat_database;'
                              'Trusted_Connection=yes;')
        print("sql connexion reussie")
    except:
        print("sql connexion échouée")

    try:
        q=query_sentence
        print(q)
        cursor = conn.cursor()
        a=cursor.execute(q)
        #print(a)
    except:
        print("connexion query échouée")
    try:
        for i in cursor:
            return i
            print(i)
    except:
        print("requete invalide")

if __name__ == '__main__':
    discut = "The following is a conversation with a respectful humwan person . The human is helpful, creative, clever,lovely, and very friendly.\nHuman: what is your name?\nAI: I am the Agent Espoir\nHuman: okay\nAI:you're welcome, it's my duty to satisfy your requests.\n\nHuman: what is the price of the product?\nAI: please,give us the name of the product \nHuman: Iphone 10 \nAI:the price of the Iphone 10 is.\nHuman: how much does the product cost?\nAI:please, you want to know the price of which product?\nHuman:iphone 11\n\nAI:the price of the Iphone 11 is.\nHuman:okay cool!\nHuman: what is the status of my order please?\nAI:Can you give us your order number please?\nMy order number is sdfoen47\nThe status of your order is\nHuman:Okay cool!\nHuman:Bonjour, j'aimerais savoir le pourquoi dont jusque là j'ai pas reçu ma commande?\nAI: S'il vous plaît ,donnez nous votre numéro de commande\nHuman:mon numéro de commande est dieD147\nAI: le status de votre commande est \nokay thanks\n\nHuman:  "
    app.run(host='0.0.0.0', port='8888', debug=True)