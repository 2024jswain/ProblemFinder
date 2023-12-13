from openai import OpenAI
import pandas as pd

class GPTanalysis:

    def __init__(self, key):

        self.client = OpenAI(api_key=key)

    
    def testKey(self):

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "testing key"}])
            
            return True
        
        except Exception as e:
            print(e)
            return False


    def GPTinsight(self, df):

        reviewText = []

        for i, row in df.iterrows():
            reviewText.append("ID: " + str(i) + " Review: " +  row['body'])

       

        reviewsString = '|*|'.join(reviewText)
        persona = "You are a market research expert" 
        instructions = "These are negative reviews from amazon. Please reduce them into a list of the most frequent complaints with a sumnmary for each. After each complaint give the ID reviews that mention the issue"

            
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",

            messages=[
                {"role": "system", "content": persona + instructions},
                {"role": "user", "content": reviewsString}])

        return response.choices[0].message.content
    

