#1- mock
from unittest.mock import Mock

mock = Mock()
side_effect = lambda value: value + 1
mock.side_effect = side_effect

print(mock(1))
print(mock(3))
