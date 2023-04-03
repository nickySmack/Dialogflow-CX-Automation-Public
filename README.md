

# REQUIRED MODULES:
- google-cloud-dialogflow-cx
- pandas
- requests-oauthlib

# USE:
1. Modify config.ini to match the correct settings from your CX instance
2. In root folder have 'entities.csv' and/or 'intents.csv' following same format as the one provided in this repo.
3. In root folder have 'credentials.json' which is a download of service account credentials from Google Cloud IAM. 
4. Run the script and verify that your new entity values are created in CX.

# Google API used:
https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/patch
https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/create
https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/create
