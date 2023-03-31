#Credits Lasya Priyanka, https://stackoverflow.com/users/17016521/lasya-priyanka on stackoverflow for the idea and framework

# requirements:
# google-cloud-dialogflow-cx
# pandas
# requests-oauthlib

import pandas as pd
import json
import configparser
from google.oauth2 import service_account
from google.cloud.dialogflowcx_v3beta1.types import entity_type
from google.auth.transport.requests import AuthorizedSession

# grab config
config = configparser.ConfigParser()
config.read('config.ini')

# read the CSV file into a Pandas DataFrame
df = pd.read_csv('entities.csv')

# initialize an empty list to hold the JSON blobs
json_blobs = []

# loop through each row of the DataFrame
for index, row in df.iterrows():

    # get the value name and synonyms from the current row
    value = str(row['serviceTypeId'])
    synonyms = [str(row[col]).replace('\u00a0', ' ') for col in row.index[1:] if not pd.isna(row[col])]
    
    # create a dictionary with the value and synonyms
    blob = {'value': value, 'synonyms': synonyms}
    
    # append the dictionary to the list of JSON blobs
    json_blobs.append(blob)

# print json for testing if needed
json_string = json.dumps(json_blobs)
# print(json_string)

# configure service account creds
# you must have a file credentials.json in root folder of this script
# you can get the credentials.json from google cloud IAM > service accounts
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json')
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])
authed_session = AuthorizedSession(scoped_credentials)





# CX variables (entity guid needed if you are updating an existing)
# these are grabbed from config.ini but they should be easy to get from your CX instance
project_id = config.get('cx', 'project_id')
agent_id = config.get('cx', 'agent_id')
location = config.get('cx', 'location')
entity = config.get('cx', 'entity')
kind = entity_type.EntityType.Kind.KIND_MAP # could probably just string "KIND_MAP but have not tested"
response = authed_session.patch('https://dialogflow.googleapis.com/v3/projects/'+ project_id + '/locations/' + location + '/agents/' + agent_id + '/entityTypes/' + entity,
                    json={
                            "displayName": "serviceTypeId", # todo: make this reflect name of .csv file
                            "kind": kind,
                            "entities": json_blobs
                        }
                    )                        

response_txt = response.text
print(response_txt)
