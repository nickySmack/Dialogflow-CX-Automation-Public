# Dialogflow-CX-Entity-Patch
This is a py script to update existing dialogflow entites from a csv. Allows for outsourcing of synonyms to other less technical users, or just easier administration for yourself.

# REQUIRED MODULES:
- google-cloud-dialogflow-cx
- pandas
- requests-oauthlib

# USE:
1. Modify config.ini to match the correct settings from your CX instance
2. In root folder have 'entities.csv' following same format as the one provided in this repo. Modify Values, Names, and Synonyms as needed. Names is more for a clean readable entity name that might relate to an ID from an API service or similar. In my use case the serviceTypeId is the what everything maps back to. Change as desired.
3. In root folder have 'credentials.json' which is a download of service account credentials from Google Cloud IAM. 
4. Run the script and verify that your new entity values are created in CX.

# Google API used:
https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/patch
