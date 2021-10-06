from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
import os
from datetime import datetime
import requests
import json
import socket
import pytz
import tweepy
from newsapi import NewsApiClient

#gets current time
tz_Bangkok = pytz.timezone("Asia/Bangkok")
now = datetime.now(tz_Bangkok)
#Finds the location of the user
IP = socket.gethostbyname(socket.gethostname())


#open weather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = BASE_URL + "q=" + "Bangkok" + "&appid=" + "9b40b1eecc6c6d49bfd11e1f14f3c5a2"
#weather API, because for some reason open weather does not have chance of rain built in
response_call = requests.get("https://api.weatherapi.com/v1/forecast.json?key=d41114c6bb5c4317917125853212809&q=Bangkok&days=1&aqi=yes&alerts=yes")
g = response_call.json()

# HTTP request
response = requests.get(URL)
if response.status_code == 200:
   data = response.json()
#all the info needed
   main = data['main']
   weather = data['weather'][0]
   temperature = main['temp']
   feels_like = main['feels_like']
   humidity = main['humidity']
   pressure = main['pressure']
   detail = g["forecast"]["forecastday"][0]["hour"][int(now.strftime("%H"))]["condition"]["text"]
   visibility = data['visibility']
   cor = g["forecast"]["forecastday"][0]["hour"][int(now.strftime("%H"))]["chance_of_rain"]
   humidity = g["forecast"]["forecastday"][0]["hour"][int(now.strftime("%H"))]["humidity"]
   wind = g["forecast"]["forecastday"][0]["hour"][int(now.strftime("%H"))]["gust_kph"]
temp = int((float(temperature) - 273.15))
feels_like = int((float(feels_like) - 273.15))
visibility = round((visibility / 100), 1)

#part 2 twitter trends that's life
#Thailand's WOEID = 23424960
consumer_key ="LaxYmCw8MCecbFaKQhZ9G1yFS"
consumer_secret = "Tdy6CHiLgoBS4byxYHZOFlEtXU4pCkq3v8ebVhlPKG3t5ADnmO"
accessToken = "2992423021-76oS6pWDG6SctRDfQE7T3v3N1PqocX3kj6E5JDJ"
accessTokenSecret = "ypWIgnuKEKoJvJZfe6MWyzEcptfuwrKX8b7KQv5UGBVDo"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessTokenSecret)
API = tweepy.API(auth)
WOEID = "23424960"
trends = API.get_place_trends(WOEID)[0]["trends"]
short_trends = []
for i in range(len(trends)):
    if len(trends[i]["name"]) < 15:
        if "#" in trends[i]["name"]:
            short_trends.append(trends[i])
    else:
        pass

colu1 = []
colu2 = []
switch = True
MAX_ITEMS = 8
for headline in short_trends:
    if len(colu1) + len(colu2) == 8:
        break
    if switch == True:
        colu1.append(headline)
        switch = False
    else:
        colu2.append(headline)
        switch = True

#part3 news_api
newsapi = NewsApiClient(api_key='bc3299ee38ad4b349e402d6986a01bbf')
top_headlines = newsapi.get_top_headlines(sources='bbc-news',
                                          language='en',)
top_headlines = top_headlines["articles"]


#part4 covid numbers
covid_numbers = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"
opening = requests.get(url= covid_numbers)
result = opening.json()
new_cases = "{:,}".format(int(result[0]['new_case']))
new_death = "{:,}".format(int(result[0]['new_death']))
new_recover = "{:,}".format(int(result[0]['new_recovered']))


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    return render_template("index.html",
    repo = humidity, temp = temp,
    feels_like = feels_like, detail = detail,
    visibility = visibility, cor = cor,
    humidity = humidity, wind = wind,
    new_cases = new_cases, new_death = new_death,
    new_recover = new_recover, trends1 = colu1,
    trends2 = colu2, article = top_headlines)