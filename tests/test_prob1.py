import unittest
import prob1
import requests

class TestProb1(unittest.TestCase):

    def setup(self):
        pass
    
    def test_endpoint_connection(self):
        MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
        test_url = 'https://backend-candidate-homework.lola.co/problem/part_1'
        headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

        request =  requests.get(test_url, headers=headers)
        self.assertEqual(request.status_code, requests.codes.ok)
        self.assertEqual(type(request.json()), dict)
    
    def test_prob1_correct(self):
        answer = prob1.main()
        self.assertEqual(type(answer), dict)
        output_correct = answer.get('correct')
        self.assertEqual(output_correct, True)
    
    # can write tests for the utility functions just to make sure they work the way that's expected checkcheck


if __name__ == '__main__':
    unittest.main()

