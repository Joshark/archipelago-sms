from unittest import TestCase
import bit_helper

class Test(TestCase):
    def test_extract_bits(self):
        val = bit_helper.extract_bits(0x40, 11)
        print(val)
        assert(val.__contains__(94))
