import unittest
from decimal_to_binary import get_converted_bin


class Test(unittest.TestCase):

    def setUp(self):
        self.setup = {
            12: '1100',
            19: '0001 0011',
            179: '1011 0011',
            255: '1111 1111',
            248237: '0011 1100 1001 1010 1101',
            829402: '1100 1010 0111 1101 1010'
        }

    def test_function(self):
        for k, v in self.setup.items():
            result = get_converted_bin(k, ' ')
            self.assertEqual(result, v)

