"""
Utilities2 Module
"""
import datetime
import json
import requests

def get_payload(test_url, headers):
    """
    Gets JSON payload from API endpoint; throws error if connection fails.
    Returns the JSON payload.
    """
    request = requests.get(test_url, headers=headers)

    request.raise_for_status() #throws an exception if connections fails

    return request.json()

def determine_return_legs(payload):
    outbound_leg_id = payload['arguments']['outbound_leg_id']

    viable_return_legs = set()
    for leg in payload['input']['fares']:
        if leg['legs'][0] == outbound_leg_id:
            viable_return_legs.add(leg['legs'][1])
    
    return list(viable_return_legs)

def post_response(payload, test_url, headers, viable_legs):
    """
    POST the total time in seconds to the API endpoint.
    Return the response from the POST request. 
    """
    result_token = payload['token']
    response = {"header": {"token": result_token}, "data": {"return_leg_ids": viable_legs}}

    return requests.post(test_url, headers=headers, data=json.dumps(response))