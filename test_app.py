import unittest
from flask import Flask
from my_app import demoapp  # Replace with the actual name of your Flask app file

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = demoapp.test_client()
        self.app.testing = True

    def test_get_data(self):
        # Send a GET request to the '/api/data' endpoint
        response = self.app.get('/api/data')

        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the response data matches the expected output
        expected_data = {'message': 'Hello, World!', 'status': 'success'}
        self.assertEqual(response.json, expected_data)

if __name__ == '__main__':
    unittest.main()
