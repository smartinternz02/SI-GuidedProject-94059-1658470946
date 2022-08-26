import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "7Y0HoWPElQ9JLR-rhBQgwr6Mo7DPMweNGT5xZJFroOtb"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['a1','a2','a3','a4','a5','a6','a7','Type','Calories','Protien','Fat','Sodium','Fiber','Carbo','Sugars','Potass','Vitamins','Shelf','Weight','Cups'], "values": [[0,   1,   0,   0,   0,   0,   0,   0,
       100,   2,   1, 140,   2,  11,  10, 120,
        25,   3,   1,   0.75]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a8fecb2a-e01c-4d94-8ccd-b9f33da4b6bc/predictions?version=2022-07-28', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())