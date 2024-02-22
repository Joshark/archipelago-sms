from unittest import TestCase
import bit_helper

class Test(TestCase):
    def test_extract_bits(self):
        val = bit_helper.extract_bits(0x40, 11)
        assert(val.__contains__(94))

    def test_bit_flagger(self):
        val = bit_helper.bit_flagger(0x0, 7, True)
        assert(val == 0x80)
