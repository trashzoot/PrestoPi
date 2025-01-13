import requests
import json
from urlencode import urlencode
import binascii
import time

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


def check_tokenexp(token):
    # Split the token into its three parts
    parts = token.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid JWT token format")
    
    # Base64 decode the payload (middle part)
    payload_b64 = parts[1]
    # Add padding if necessary
    payload_b64 += '=' * ((4 - len(payload_b64) % 4) % 4)
    payload_bytes = binascii.a2b_base64(payload_b64)
    
    # JSON decode the payload
    payload = json.loads(payload_bytes)
    
    #check expiry against current and return True if token expired
    if time.time() > payload["exp"]:
        return True
    else:
        return False
    
