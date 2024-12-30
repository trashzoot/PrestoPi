import requests
import json
from urlencode import urlencode

def get_access_token(tenant_id, client_id, client_secret, username, password):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headerdata = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    bodydata = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
        "scope": "https://graph.microsoft.com/.default"
    }
    
    data = urlencode(bodydata)

    token_data = requests.request("POST", url, data = data, headers = headerdata).json()

    return token_data["access_token"]

def make_graph_request(access_token, endpoint):
    url = f"https://graph.microsoft.com/v1.0/{endpoint}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response


