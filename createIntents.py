import configparser
import csv
import json
from google.cloud import dialogflowcx_v3beta1 as dialogflow
from google.oauth2 import service_account

# read the configuration values from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
google_cx_agent_guid = config['cx']['agent_id']
project_id = config['cx']['project_id']
authentication_file_path = config['DEFAULT']['authentication_file_path']

# auth
with open(authentication_file_path, 'r') as f:
    credentials_info = json.load(f)
credentials = service_account.Credentials.from_service_account_info(credentials_info)
client = dialogflow.IntentsClient(credentials=credentials)

# create a helper function to create an intent in CX, repeat_count must exist or error is thrown
def create_intent(intent_name, training_phrases_parts):
    training_phrases = []
    for training_phrase_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrase_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part], repeat_count=1)
        training_phrases.append(training_phrase)

    intent = dialogflow.Intent(
        display_name=intent_name,
        training_phrases=training_phrases,
    )

    parent = f"projects/{project_id}/locations/global/agents/{google_cx_agent_guid}"
    response = client.create_intent(request={"parent": parent, "intent": intent})
    print(f'Intent "{response.display_name}" created with ID "{response.name.split("/")[-1]}".')

   
    
# read the intents from the CSV file and create them in CX
with open('intents.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        intent_name = row[0]
        training_phrases = [phrase for phrase in row[1:] if phrase != '']
        create_intent(intent_name, training_phrases)
