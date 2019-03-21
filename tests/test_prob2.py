"""
Unittest Module for Problem 2
"""
import unittest
import prob2
import requests
import util.utilities2 as util


class TestProb2(unittest.TestCase):

    def setup(self):
        pass

    def test_endpoint_connection(self):
        MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
        test_url = 'https://backend-candidate-homework.lola.co/problem/part_2'
        headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

        self.assertEqual(type(util.get_payload(test_url, headers)), dict)

        MY_TOKEN = ''
        headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

        with self.assertRaises(requests.exceptions.HTTPError):
            util.get_payload(test_url, headers)

    def test_determine_return_legs(self):

        with self.assertRaises(TypeError):
            util.determine_return_legs([])

    def test_prob2_correct(self):
        answer = prob2.main()
        self.assertEqual(type(answer), dict)
        output_correct = answer.get('correct')
        self.assertEqual(output_correct, True)


if __name__ == '__main__':
    unittest.main()
