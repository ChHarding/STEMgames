#In this file I will scrape the data from STEAM reviews using the API. 
#Start by building list of games. 
import steamreviews

request_params = dict()
request_params['filter'] = 'updated'
request_params['day_range'] = '365'
request_params['language'] = 'english'
steamreviews.download_reviews_for_app_id_batch(chosen_request_params=request_params)
                                                                