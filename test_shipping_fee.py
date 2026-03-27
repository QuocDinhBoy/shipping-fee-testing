import unittest
from calculate_shipping_fee import calculate_total_shipping_fee
class TestCalculateTotalShippingFee(unittest.TestCase):

#Kiểm thử biên
    def test_BV_1(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(-0.1, 300000, False, False)

    def test_BV_2(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(0, 300000, False, False)

    def test_BV_3(self):
        self.assertEqual(
            calculate_total_shipping_fee(0.1, 300000, False, False),
            0
        )

    def test_BV_4(self):
        self.assertEqual(
            calculate_total_shipping_fee(2.9, 300000, False, False),
            0
        )

    def test_BV_5(self):
        self.assertEqual(
            calculate_total_shipping_fee(3.0, 300000, False, False),
            0
        )

    def test_BV_6(self):
        self.assertEqual(
            calculate_total_shipping_fee(3.1, 300000, False, False),
            15500
        )

    def test_BV_7(self):
        self.assertEqual(
            calculate_total_shipping_fee(99.9, 300000, False, False),
            499500
        )

    def test_BV_8(self):
        self.assertEqual(
            calculate_total_shipping_fee(100, 300000, False, False),
            500000
        )

    def test_BV_9(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(100.1, 300000, False, False)

    def test_BV_10(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(5, -1000, False, False)

    def test_BV_11(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(5, 0, False, False)

    def test_BV_12(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 1000, False, False),
            35000
        )

    def test_BV_13(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 199000, False, False),
            35000
        )

    def test_BV_14(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 200000, False, False),
            25000
        )

    def test_BV_15(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 200001, False, False),
            25000
        )
    
    def test_BV_16(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 300000, True, False),
            33000
        )

    def test_BV_17(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 300000, False, True),
            37000
        )
    
#Kiểm thử với độ đo C2
    def test_C2_1(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(-1, 300000, False, False)

    def test_C2_2(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(101, 300000, False, False)

    def test_C2_3(self):
        with self.assertRaises(ValueError):
            calculate_total_shipping_fee(2, -1, False, False) 

    def test_C2_4(self):
        self.assertEqual(
            calculate_total_shipping_fee(5, 300000, False, False),
            25000
        )

    def test_C2_5(self):
        self.assertEqual(
            calculate_total_shipping_fee(2, 100000, True, True),
            30000
        )        

if __name__ == "__main__":
    unittest.main()