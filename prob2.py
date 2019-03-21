"""
Prob2 Module
"""
import datetime
import json
import requests
import sys
from util import utilities2 as util


def main():
    """
    GETs JSON Payload from API endpoint, determines viable return-leg ids for a given outbound-leg id.
    POSTs result to same endpoint.
    """

    MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
    test_url = 'https://backend-candidate-homework.lola.co/problem/part_2'
    headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

    # Activate sample mode by passing 'sample' at command line

    if len(sys.argv) > 1 and sys.argv[1] == 'sample':
        test_url += '?sample=true'

    # GET payload and determine viable return-leg ids

    request = util.get_payload(test_url, headers)

    viable_legs = util.determine_return_legs(request)

    # POST response

    result = util.post_response(request, test_url, headers, viable_legs)

    print(result.json())

    return(result.json())


if __name__ == '__main__':
    main()
