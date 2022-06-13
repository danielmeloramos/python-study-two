#1- mock - patch (decorator)
import unittest
from unittest.mock import patch, mock_open
from client import do

class TestExample(unittest.TestCase):
    @patch("client.open", new_callable=mock_open, read_data="data")
    def test_example(self, mock_open):
        response = do("teste")
        self.assertEqual(response, "data")

