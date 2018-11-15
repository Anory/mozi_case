import unittest
from demo import mozirun
import requests
import time
import json


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.run = mozirun.RunMozi()

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
