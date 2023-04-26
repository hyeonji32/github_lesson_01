import unittest
import dec_2_hex as dh

# unittest를 이용한 테스트
class TestDecimalToHexadecimal(unittest.TestCase):

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(dh.decimal_to_hexadecimal(255), "FF")
        self.assertEqual(dh.decimal_to_hexadecimal(65535), "FFFF")
        self.assertEqual(dh.decimal_to_hexadecimal(16), "10")
        self.assertEqual(dh.decimal_to_hexadecimal(0), "0")

if __name__ == '__main__':
    unittest.main()
