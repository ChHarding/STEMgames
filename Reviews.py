#In this file I will scrape the data from STEAM reviews using the API. 
#Start by building list of games. 
import steamreviews
steamreviews.download_reviews_for_app_id_batch()
