from urllib.request import urlopen
import urllib
import time
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests
import nltk 
import pprint
"""
steampage = BeautifulSoup(urllib.request.urlopen('http://store.steampowered.com/stats/?l=english').read())

timestamp = time.time()
currentTime = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

top100CSV = open('SteamTop100byTime.csv', 'a')

for row in steampage('tr', {'class': 'player_count_row'}):
    steamAppID = row.a.get('href').split("/")[4]
    steamGameName = row.a.get_text().encode('utf-8')
    currentConcurrent = row.find_all('span')[0].get_text()
    maxConcurrent = row.find_all('span')[1].get_text()
    
    top100CSV.write('{0},{1},"{2}","{3}","{4}"\n'.format(currentTime, steamAppID, steamGameName, currentConcurrent, maxConcurrent))

top100CSV.close()
"""
column_names = ["Timestamp", "AppID", "Title", "Current_Players", "Peak_Players"]
df = pd.read_csv("SteamTop100byTime.csv", names=column_names)
appids_list = df.AppID.to_list()
df.to_csv('top100appids.csv') 

def get_reviews(appid, params): 
        url_start = 'https://store.steampowered.com/appreviews/'
        try:
            response = requests.get(url=url_start+str(appid), params=params, headers={'User-Agent': 'Mozilla/5.0'})
        except:
                return {'reviews' : []}
        return response.json() # return data extracted from the json response

reviews = []
cursor = '*'
params = { # https://partner.steamgames.com/doc/store/getreviews
    'json' : 1,
    'filter' : 'all', # sort by: recent, updated, all (helpfulness)
    'language' : 'english', # https://partner.steamgames.com/doc/store/localization
    'day_range' : 9223372036854775807, # shows reviews from all time
    'review_type' : 'all', # all, positive, negative
    'purchase_type' : 'all', # all, non_steam_purchase, steam
    'num_per_page' : 50,
    'cursor' : '*'.encode()
}


app_dict = {}
app_ids = (appids_list)
for i, app_id in enumerate(app_ids):
    l = get_reviews(app_id, params)['reviews']
    app_dict[app_id] = l

STEM_words  = ["game", "player", "scientific", "biological", "learning", "education", "historical"]
#app_freq[123] = {"game":2, "player":3
app_freq = {}
scraped_apps = list(app_dict.keys())
for a in scraped_apps:
    rl = app_dict[a]
    d = {sw:0 for sw in STEM_words}
    for i,r in enumerate(rl):
        rev_str = r["review"]
        #print("***", len(rev_str))
        words = nltk.word_tokenize(rev_str)
        lwords = [w.lower() for w in words]
        for sw in STEM_words:
            if sw in lwords:
                #print(a, i,"found", sw)
                d[sw] = d[sw] + 1
    app_freq[a] = d

df = pd.DataFrame.from_dict(app_freq, orient="index")
df.to_csv("PopularSTEMterms.csv")











