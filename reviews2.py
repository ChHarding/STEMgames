#this program is based on the GetAppList available on the Steam store. It allows me to create a pkl with all game reviews without having to create a list of ids first. 
# The script is able to download the file but I cannot see the IDs. Tweaked code at the end to add appid. 
import pandas as pd
import requests
#dark souls 570940
#simcity 4 24780
#mass effect 1328670

"""
response = requests.get(r'https://api.steampowered.com/ISteamApps/GetAppList/v2/')
app_ids_df = pd.DataFrame(response.json()['applist']['apps'])
app_ids_df.to_csv("apps_ids.csv")
app_ids_df

print(app_ids_df)

app_ids = app_ids_df['appid'].to_numpy()
app_ids, len(app_ids)
"""

column_names = ["", "appid", "name"]
df = pd.read_csv("apps_ids.csv", names=column_names)
appids_list = df.appid.to_list()


 
#STEP 2. Get reviews. The reviews for the STEAM games are sorted by helpfulness. I only look at English reviews, both positive and negative. I select the 50 most helpful. 
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
    'filter' : 'all', # sort by: recent, updated, all (helpfullness)
    'language' : 'english', # https://partner.steamgames.com/doc/store/localization
    'day_range' : 9223372036854775807, # shows reveiws from all time
    'review_type' : 'all', # all, positive, negative
    'purchase_type' : 'all', # all, non_steam_purchase, steam
    'num_per_page' : 50,
    'cursor' : '*'.encode()
          }

app_ids = (appids_list)

for i, app_id in enumerate(app_ids):
    reviews += get_reviews(app_id, params)
    if (i+1)%500 == 0:
        print(f'{i+1} of {len(app_ids)}: {len(reviews)} reviews')


reviews_df = pd.DataFrame(reviews)[["review", "voted_up", "weighted_vote_score"]]
reviews_df.dropna(inplace=True)
reviews_df.reset_index(inplace=True)
reviews_df

reviews_df.to_csv(r'C:\Users\UTEC\Desktop\hci584\HCI584 - STEM games\STEMgames\rawreviews.csv')

