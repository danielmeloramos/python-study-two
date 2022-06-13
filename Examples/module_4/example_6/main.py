#1- mock
from unittest.mock import Mock

mock = Mock()
mock.side_effect = [1, 2]

print(mock())
print(mock())
