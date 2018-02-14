import unittest

from app import app

class Test(unittest.TestCase):
    def test(self):
        result = app.test_client().get('/')

        self.assertEqual(result.data.decode('utf-8'), 'Hello Kryptopal !!')