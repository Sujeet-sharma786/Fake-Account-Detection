import dataAPI
from dataAPI import data_fetch
import pickle
import numpy as np
import warnings
import firebase_admin
import firebase
import sys
from firebase_admin import db
import tweepy
import model
warnings.filterwarnings("ignore")
try:
    dectree=pickle.load(open('model.pkl','rb'))
except FileNotFoundError:
    model.train_model()
    dectree=pickle.load(open('model.pkl','rb'))


def pred(features):
    input_data = input_data = np.column_stack(features)
    result = dectree.predict(input_data)
    if 1 in result:
        return True
    else:
        return False
    


def action(username):
    if username[0] == "@":
        username = username[1:]
    if "https://twitter.com/" in username:
        username = username[20:]
    elif"twitter.com/" in username:
        username = username[12:]
    username = username.lower()
    ref = db.reference("/")
    stored_rec = ref.get()
    try:
        data = data_fetch(username)
    except tweepy.NotFound:
        return "Account not found"
    except tweepy.Forbidden:
        return "Account has been suspended"
    output=pred(data)
    ref = db.reference(f"/{username}")
    if output == True :ref.set("Real")
    else : ref.set("Fake")
    if output:
        return 'Real'
    else:
        return 'Fake'
print(action(sys.argv[1]))