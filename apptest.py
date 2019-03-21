import requests
import json

MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
test_url = 'https://backend-candidate-homework.lola.co/problem/test'
headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

request =  requests.get(test_url, headers=headers).json()

mult_result= request['input']['number'] * request['arguments']['multiplier']
result_token = request['token']
response = {"header": {"token": result_token}, "data": {"multiplication_result": mult_result}}

print(response)
r = requests.post(test_url, headers=headers, data=json.dumps(response))

print(r.text)

