#1- mock
from unittest.mock import Mock

mock = Mock()
mock.side_effect = Exception("Err")

print(mock())
