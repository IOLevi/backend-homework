"""
Unittest Module for Problem 2
"""
import unittest
import prob2
import requests

class TestProb2(unittest.TestCase):

    def setup(self):
        pass
    
    
    def test_prob2_correct(self):
        answer = prob2.main()
        self.assertEqual(type(answer), dict)
        output_correct = answer.get('correct')
        self.assertEqual(output_correct, True)
    
    # can write tests for the utility functions just to make sure they work the way that's expected checkcheck


if __name__ == '__main__':
    unittest.main()
