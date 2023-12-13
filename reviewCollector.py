import requests
import json
import pandas as pd


class reviewCollector:

    def __init__(self, apiKey):

        self.key = apiKey


    def testKey(self):

        params = {
                'api_key': self.key,
                'type': 'search',
                'search_term': 'test',
                'amazon_domain': 'amazon.com'}

        try: 
            api_result = requests.get('https://api.asindataapi.com/request', params)
            return True

        except Exception as e:
            print(e)
            return False
                
        


    def getReview(self, asin):

        params = {
            'api_key': self.key,
            'type': 'reviews',
            'asin': asin,
            'amazon_domain': 'amazon.com',
            'reviewer_type' : 'verified_purchase',
            'review_stars' : 'all_critical',
            'sort_by' : 'most_helpful'
            }


        api_result = requests.get('https://api.asindataapi.com/request', params)

        return api_result.json()['reviews']


    def getReviews(self, product, reviewsPerItem = 5):

        params = {
            'api_key': self.key,
            'type': 'search',
            'search_term': product,
            'amazon_domain': 'amazon.com'
            }

        api_result = requests.get('https://api.asindataapi.com/request', params)

        data = [self.getReview(product["asin"]) for product in api_result.json()["search_results"][: reviewsPerItem - 1]]
        data = [item for sublist in data for item in sublist]
        df = pd.DataFrame(data)


        return df




