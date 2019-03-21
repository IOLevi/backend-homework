"""
Utilities1 Module
"""
import datetime
import json
import requests


def iso_to_datetime(input_str):
    """
    Removes final colon from input string to conform to python 3.6 %z format specifier.
    Returns a datetime object based on the ISO input string.
    """
    format = '%Y-%m-%dT%H:%M:%S%z'

    if input_str[22] != ':':
        raise ValueError(
            'Invalid format. Expected colon at position 22 in input string')
    input_str = input_str[0:22] + input_str[23:]
    return datetime.datetime.strptime(input_str, format)


def populate_times(payload, legs):
    """
    Creates lists of departures and arrival datetimes for each leg in a fare using binary search.
    Returns depature list and arrival list as a tuple. 
    """
    if not isinstance(payload, dict):
        raise TypeError('Payload expected type is Dict.')

    if not isinstance(legs, list):
        raise TypeError('Legs expected type is List')

    if len(legs) != 2:
        raise ValueError("Legs expected to be length 2")

    dept_list = []
    arrv_list = []

    def binary_search_populate(arr, target):
        """
        Binary search through legs array. When matched against target leg, appends associated
        departure and arrival time to the dept and arrival lists as datetime objects.
        """
        first = 0
        last = len(arr) - 1
        while first <= last:
            mid = (first + last) // 2
            mid_value = arr[mid]['id']

            if mid_value == target:
                dept_list.append(iso_to_datetime(
                    arr[mid]['departure_utc']['iso']))
                arrv_list.append(iso_to_datetime(
                    arr[mid]['arrival_utc']['iso']))
                return
            elif mid_value < target:
                first = mid + 1
            else:
                last = mid - 1

        raise ValueError("Couldn't find target leg in list.")

    all_legs = payload['input']['legs']
    for leg in legs:
        binary_search_populate(all_legs, leg)

    return dept_list, arrv_list


def get_leg_ids(payload):
    """
    Binary searches through fares list.
    Returns the list of legs associated with the fare_id.
    """

    if not isinstance(payload, dict):
        raise TypeError('Payload expected type is Dict')

    fare_id = int(payload['arguments']['fare_id'][5:])
    if not isinstance(fare_id, int):
        raise ValueError('Failed to retrieve fare_id from payload')

    def binary_search(arr):
        """
        Binary search of fares array.
        Returns list of legs if found; throws exception if fare_id not in list.
        """
        first = 0
        last = len(arr) - 1
        while first <= last:
            mid = (first + last) // 2
            mid_value = int(arr[mid]['id'][5:])

            if mid_value == fare_id:
                return arr[mid]['legs']
            elif mid_value < fare_id:
                first = mid + 1
            else:
                last = mid - 1

        raise ValueError("Couldn't find fare_id in list")

    fares = payload['input']['fares']
    return binary_search(fares)


def calc_total_time(dept_list, arrv_list):
    """
    Calculates total flight time between legs in departure and arrival lists in total seconds.
    Returns total time in seconds as an integer.
    """

    if not isinstance(dept_list, list) or not isinstance(arrv_list, list):
        raise TypeError("Arguments expected to be of type List")

    total_time = 0
    for dept, arv in zip(dept_list, arrv_list):
        total_time += int((arv - dept).total_seconds())

    return total_time


def get_payload(test_url, headers):
    """
    Gets JSON payload from API endpoint; throws error if connection fails.
    Returns the JSON payload.
    """
    request = requests.get(test_url, headers=headers)

    request.raise_for_status()  # throws an exception if connections fails

    return request.json()


def post_response(payload, test_url, headers, total_time):
    """
    POST the total time in seconds to the API endpoint.
    Return the response from the POST request. 
    """
    result_token = payload['token']
    response = {"header": {"token": result_token},
                "data": {"total_seconds": total_time}}

    return requests.post(test_url, headers=headers, data=json.dumps(response))
