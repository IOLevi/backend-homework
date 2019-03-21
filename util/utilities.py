"""
Utilities Module
"""
import datetime
def iso_to_datetime(input_str):
    """
    Removes final colon from string to conform to python 3.6 %z format specifier.
    Returns a datetime object based on the ISO input string.
    """
    format = '%Y-%m-%dT%H:%M:%S%z'

    loc = input_str.rfind(":")
    if loc == -1:
        raise ValueError('Invalid input format') #probably change this since rfind will ultimate get the colon
    input_str = input_str[0:loc] + input_str[loc + 1:]
    return datetime.datetime.strptime(input_str, format)

def populate_times(payload, legs):
    """
    Creates a list of departures datetimes and a list of arrivals datetimes for each leg in a fare.
    Returns depature list and arrival list as a tuple. 
    """
    dept_list = []
    arrv_list = []
    for leg in payload['input']['legs']: #could use a search function to make this faster
        if leg['id'] in legs:
            dept_list.append(iso_to_datetime(leg['departure_utc']['iso']))
            arrv_list.append(iso_to_datetime(leg['arrival_utc']['iso']))
    
    return dept_list, arrv_list

def get_leg_ids(payload, fare_id):
    """
    Searches through fares list, returns the list of legs associated with the fare_id.
    """
    for fare in payload['input']['fares']: #could use a search function to make this faster?
        if fare['id'] == fare_id:
            return fare['legs'] # list of legs
    raise ValueError('Could find fare associated with fare ID')

def calc_total_time(dept_list, arrv_list):
    """
    Calculates total flight time between legs in departure and arrival lists in total seconds.
    Returns total time in seconds as an integer.
    """
    total_time = 0
    for dept, arv in zip(dept_list, arrv_list):
        total_time += int((arv - dept).total_seconds())
    
    return total_time

