"""
Unittest module for Problem 1
"""
import datetime
import unittest
import prob1
import requests
import util.utilities1 as util


class TestProb1(unittest.TestCase):

    def setup(self):
        pass

    def test_endpoint_connection(self):
        MY_TOKEN = 'b2eeef5b2984468ca94b074412611815'
        test_url = 'https://backend-candidate-homework.lola.co/problem/part_1'
        headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

        self.assertEqual(type(util.get_payload(test_url, headers)), dict)

        MY_TOKEN = ''
        headers = {'X-Lola-Homework-Access-Token': f'{MY_TOKEN}'}

        with self.assertRaises(requests.exceptions.HTTPError):
            util.get_payload(test_url, headers)

    def test_iso_to_datetime(self):
        with self.assertRaises(ValueError):
            util.iso_to_datetime("2018-11-29T13:30:00+0000")

        self.assertEqual(type(util.iso_to_datetime(
            "2018-11-29T13:30:00+00:00")), datetime.datetime)

    def test_populate_datetimes(self):
        with self.assertRaises(ValueError):
            util.populate_times({}, [])
        with self.assertRaises(TypeError):
            util.populate_times([], [])
        with self.assertRaises(TypeError):
            util.populate_times({}, {})

    def test_get_leg_ids(self):
        with self.assertRaises(TypeError):
            util.get_leg_ids([])

    def test_calc_total_time(self):
        with self.assertRaises(TypeError):
            util.calc_total_time({}, [])
            util.calc_total_time([], {})

        dept = [datetime.datetime(
            2018, 11, 29, 7, 0, tzinfo=datetime.timezone.utc)]
        arv = [datetime.datetime(
            2018, 11, 29, 7, 10, tzinfo=datetime.timezone.utc)]

        self.assertEqual(util.calc_total_time(dept, arv), 600)

    def test_prob1_correct(self):
        answer = prob1.main()
        self.assertEqual(type(answer), dict)
        output_correct = answer.get('correct')
        self.assertEqual(output_correct, True)


if __name__ == '__main__':
    unittest.main()
