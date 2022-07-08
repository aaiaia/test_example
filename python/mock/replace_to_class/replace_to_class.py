import unittest
from unittest.mock import patch, MagicMock

class DummyClass():
    def __init__(self, num):
        self.num = num

    def dummy_function(self):
        if self.num == 0:
            return '0'
        elif self.num == 1:
            return '1'
        elif self.num >= 4 and self.num <=7:
            return str(self.num)
        else:
            return 'x'

def main():
    print('call main()')
    _mock_instance = MagicMock(side_effect=DummyClass)
    for _i in range(0, 10):
        print('_mock_instance(' + str(_i) + ') = ' + _mock_instance(_i).dummy_function())

if __name__ == '__main__':
    main()
