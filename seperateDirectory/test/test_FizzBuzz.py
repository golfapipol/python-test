import unittest
from app.FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()
    def test_input_1_should_be_1(self):
        self.assertEqual("1",self.fizzbuzz.say(1))

if __name__ == '__main__':
    unittest.main()