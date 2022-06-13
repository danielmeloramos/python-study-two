from unittest import TestCase
from unittest.mock import patch, mock_open
from client import Client

# TODO: importar o patch do módulo unittest.mock

class MockResponse:
    def __init__(self, status):
        self.status_code = status

class TestClient(TestCase):
    def setUp(self):
        self.url = "http://teste"
        self.client = Client()

    @patch('client.requests.get')
    def test_get_should_return_200_status_code(self, fake_get):
        #arrange
        expected = MockResponse(200)
        fake_get.return_value.status_code = 200 

        #action
        response = self.client.get(self.url)

        #assert
        self.assertEqual(response.status_code, expected.status_code)

    @patch('client.requests.get')
    def test_get_should_return_404_status_code(self, fake_get):
        #arrange
        expected = MockResponse(404)
        fake_get.return_value.status_code = 404 

        #action
        response = self.client.get(self.url)

        #assert
        self.assertEqual(response.status_code, expected.status_code)

    @patch('client.requests.post')
    def test_post_should_return_200_status_code(self, fake_post):
        #arrange
        expected = MockResponse(200)
        fake_post.return_value.status_code = 200 
        data = "{'is_valid' = 'true'}"

        #action
        response = self.client.post(self.url, data)

        #assert
        self.assertEqual(response.status_code, expected.status_code)

    @patch('client.requests.post')
    def test_post_should_return_400_status_code(self, fake_post):
        #arrange
        expected = MockResponse(400)
        fake_post.return_value.status_code = 400 
        data = "@"

        #action
        response = self.client.post(self.url, data)

        #assert
        self.assertEqual(response.status_code, expected.status_code)
        pass
