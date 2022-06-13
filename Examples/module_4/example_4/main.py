#1- mock
from unittest.mock import Mock

mock = Mock()
mock.return_value = 3

print(mock())
