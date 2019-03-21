"""
Probl Module
"""
import datetime
import json
import requests
import sys
from util import utilities1 as util

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

    request = util.get_payload(test_url, headers)

    legs = util.get_leg_ids(request)

    dept_times, arrv_times = util.populate_times(request, legs)

    total_time = util.calc_total_time(dept_times, arrv_times)

    # POST response

    result = util.post_response(request, test_url, headers, total_time)
    
    return(result.json())

if __name__ == '__main__':
    main()
  