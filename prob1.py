import requests
import json
import sys

MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
test_url = 'https://backend-candidate-homework.lola.co/problem/part_1'
if sys.argv[1] == 'sample':
    test_url += '?sample=true'

headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

request =  requests.get(test_url, headers=headers).json()

mult_result= request['input']['number'] * request['arguments']['multiplier']
result_token = request['token']
response = {"header": {"token": result_token}, "data": {"total_seconds": mult_result}}

print(response)
r = requests.post(test_url, headers=headers, data=json.dumps(response))

print(r.text)