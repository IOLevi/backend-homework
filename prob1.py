"""
Probl Module
"""
import requests
import json
import sys
import datetime
from util import utilities as util

def main():
    """
    GETs JSON Payload from API endpoint, calculates total airtime for each leg in fare,
    POSTs result to same endpoint.
    """ 

    MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
    test_url = 'https://backend-candidate-homework.lola.co/problem/part_1'
    headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

    # Activate sample mode by passing 'sample' at command line
    if len(sys.argv) > 1 and sys.argv[1] == 'sample':
        test_url += '?sample=true'

    # GET payload and calculate total flight time
    request =  requests.get(test_url, headers=headers).json()

    fare_id = request['arguments']['fare_id']

    legs = util.get_leg_ids(request, fare_id)

    dept_times, arrv_times = util.populate_times(request, legs)

    total_time = util.calc_total_time(dept_times, arrv_times)

    # POST response
    result_token = request['token']
    response = {"header": {"token": result_token}, "data": {"total_seconds": total_time}}

    r = requests.post(test_url, headers=headers, data=json.dumps(response))
    
    return(r.json())

if __name__ == '__main__':
    main()
  