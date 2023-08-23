'''
This class will take in a .csv file as an input and then using pandas will create lists of each column representing all of the responses to a survey. It will then send these responses thru chat gpt's api and show the user the general consensus responses to each question.

Tiz's API token: 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 (Free Trial)

'''

import requests
import pandas as pd
import json
import openai

class csvAnalyzer:
    
    # EDIT THIS
    openai.api_key = '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'
    
    
    def __init__(self,csv_filename):
        super().__init__()
        self.csv_filename = csv_filename
        #print(len(self.parseData()))
        self.gpt_response = self.send_to_gpt(self.parseData())
      
  
        
    def parseData(self):
        data_df = pd.read_csv(self.csv_filename)
        columns_list = []
        for column_name in data_df:
            column_length = len(data_df[column_name])
            col_split = column_length // 5
            
            column_data = data_df[column_name].iloc[:col_split].tolist()
            column_data.insert(0,column_name)
            columns_list.append(column_data)
            
        return str(columns_list)
        
        
    def send_to_gpt(self,data):
        prompt = '''I have a list of lists that represent survey responses. The zero-th index of each sub-list represents a 
        single question from the survey, while the rest of the indices of the list represent all of the responses submitted 
        to that survey question. For each question, can you return the question and then some sentences that represent the general
        consensus of submitted responses? All I want you to output are the question and then a summary of the responses.'''
                
        content = self.parseData() # List of lists containing all of the survey responses
        messages_1 = [{'role': 'system', 'content': prompt}] + [{'role': 'user', 'content': content}]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_1
        )

        # Extract the generated response
        chatGPT_response = response.choices[0].message.content
        
        gpt_json_response_data = json.dumps(chatGPT_response)

        
        return gpt_json_response_data
    
    
    
    def get_gpt_response(self):
        return self.gpt_response
        
        
        
        
#------------------------------------------------------

if __name__ == '__main__':
    
    filename = 'sampleData.csv'
    test = csvAnalyzer(filename)