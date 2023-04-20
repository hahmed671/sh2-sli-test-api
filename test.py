import unittest
import requests

class TestSliApi(unittest.TestCase):
    endpoint = 'https://8wk8dyslla.execute-api.ca-central-1.amazonaws.com/prod/'
    def test_http_get(self):
        r = requests.get(self.endpoint)
        self.assertEqual(r.status_code, 200)
    def test_http_post(self):
        r = requests.post(self.endpoint)
        self.assertEqual(r.status_code, 200)
    def test_http_delete(self):
        r = requests.delete(self.endpoint)
        self.assertEqual(r.status_code, 200)
if __name__ == '__main__':
    unittest.main()