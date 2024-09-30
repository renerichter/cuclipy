import requests

from params import API_TOKEN
from tools import time_to_ms

# Replace with your ClickUp API token
HEADERS = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json'
}

# Base URL for ClickUp API
BASE_URL_v2 = 'https://api.clickup.com/api/v2/'
BASE_URL_v3 = 'https://api.clickup.com/api/v3/'

def get_time_entry_in_date_range(team_id,start_date,end_date,user_id,verbose=False):
    url = BASE_URL_v2+"team/" + team_id + "/time_entries"
    query = {
    "start_date": time_to_ms(start_date),#Unix time in milliseconds
    "end_date": time_to_ms(end_date),#Unix time in milliseconds
    "assignee": user_id,#user_id
    "include_task_tags": "true",
    "include_location_names": "true",
    #"space_id": "0",
    #"folder_id": "0",
    #"list_id": "0",
    #"task_id": "string",
    #"custom_task_ids": "true",
    #"team_id": "123",
    #"is_billable": "true"
    }
    headers = {"Content-Type": "application/json","Authorization": API_TOKEN}
    response = requests.get(url, headers=headers, params=query)
    data = response.json()['data']
    if verbose:
        print(data)
    return data