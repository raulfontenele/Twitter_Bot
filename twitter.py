import tweepy
from chaves import *
from random import randint

def Autenticacao():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    return api

def Responder_Tweets(twitter_api):
    tweets = twitter_api.mentions_timeline(Retornar_Id())
    respostas = ["Oi, tudo bom?", "Diga lá meu jovem, como que tá?", "E ai, beleza?"]
    for tweet in reversed(tweets):
        Guardar_Id(tweet.id)
        twitter_api.update_status("@" + str(tweet.user.screen_name) + " " + respostas[randint(0,2)],tweet.id)

def Guardar_Id(id):
    arquivo = open("ultimoId.txt",'w')
    arquivo.write(str(id))
    arquivo.close()
    return

def Retornar_Id():
    arquivo = open("ultimoId.txt",'r')
    id = arquivo.readline()
    arquivo.close()
    return int(id)

def Main():
    twitter_api = Autenticacao()
    Responder_Tweets(twitter_api)
    
Main()
