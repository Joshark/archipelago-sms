from unittest import TestCase
from .bit_helper import extract_bits, bit_flagger

class Test(TestCase):
    def test_extract_bits(self):
        val = extract_bits(0x40, 11)
        assert(val.__contains__(94))

    def test_bit_flagger(self):
        val = bit_flagger(0x0, 7, True)
        assert(val == 0x80)
