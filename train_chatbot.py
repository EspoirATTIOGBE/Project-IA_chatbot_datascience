from random import random

import nltk
from cffi import model
from nltk.stem import  WordNetLemmatizer
lemmatizer= WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import sequential
from keras.layers import Dense,Activation,Dropout
from keras.optimizers import SGD

words=[]
classes=[]
documents=[]
ignore_words=['?','!']
data_file= open('intents.json').read()
intents=json.loads(data_file)

#parcourons l'intents , specifiquement le pattern pour tockeniser les mots(couper une phrase en de petits mots, et ensuite ajoutons-les dans la liste de mots

for intent in intents['intents']:
    for pattern in intent ['patterns']:
        w= nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append(w,intent['tag'])
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


#lemmatisons chaque mot et supprimons les mots en double de la liste
words=[lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words=sorted(list(set(words)))
classes= sorted(list(set(classes)))
print(len(documents), "documents")
print(len(classes),"classes", classes)
print(len(words), "unique lematized words", words)

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#créeons les données d'apprentissage dans lesquelles nous fournirons l'entrée et la sortie.
training=[]
output_empty=[0]*len(classes)
for doc in documents:
    bag=[]
    pattern_words=doc[0]
    pattern_words=[lemmatizer.lemmatize(word.lower())for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
        output_row=list(output_empty)
        output_row[classes.index(doc[1])]=1
        training.append([bag, output_row])
        random.shuffle(training)
        training= np.array(training)
        train_x=list(training[:,0])
        train_y=list(training[:,1])
        print("Training data created")
        #utilisons le deep neural network(réseau neuronal profond à 3 couches) pour créer notre modèle
        model.Sequential()
        model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]), activation='softmax'))
        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
        # fitting and saving the model
        hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
        model.save('chatbot_model.h5', hist)
        print("model created")