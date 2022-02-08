import unittest
from check_limits import LimitChecker, battery_is_ok
import BMSManagement as PermissibleLimit


class MyTestCase(unittest.TestCase):
    def test_battery_is_ok(self):
        temp_check = LimitChecker(25, PermissibleLimit.temperature_limit)
        soc_check = LimitChecker(70, PermissibleLimit.soc_limit)
        charge_rate_check = LimitChecker(0.7, PermissibleLimit.charge_rate_limit)
        self.assertEqual(25, temp_check.input_value)
        self.assertEqual(70, soc_check.input_value)
        self.assertEqual(0.7, charge_rate_check.input_value)
        self.assertTrue(temp_check.checkLimit())
        self.assertTrue(soc_check.checkLimit())
        self.assertTrue(charge_rate_check.checkLimit())

        # test above upper limits
        temp_check2 = LimitChecker(46, PermissibleLimit.temperature_limit)
        soc_check2 = LimitChecker(81, PermissibleLimit.soc_limit)
        charge_rate_check2 = LimitChecker(0.9, PermissibleLimit.charge_rate_limit)
        self.assertEqual(46, temp_check2.input_value)
        self.assertEqual(81, soc_check2.input_value)
        self.assertEqual(0.9, charge_rate_check2.input_value)
        self.assertFalse(temp_check2.checkLimit())
        self.assertFalse(soc_check2.checkLimit())
        self.assertFalse(charge_rate_check2.checkLimit())

        # test below lower limits
        temp_check3 = LimitChecker(-1, PermissibleLimit.temperature_limit)
        soc_check3 = LimitChecker(19, PermissibleLimit.soc_limit)
        charge_rate_check3 = LimitChecker(-1, PermissibleLimit.charge_rate_limit)
        self.assertEqual(-1, temp_check3.input_value)
        self.assertEqual(19, soc_check3.input_value)
        self.assertEqual(-1, charge_rate_check3.input_value)
        self.assertFalse(temp_check3.checkLimit())
        self.assertFalse(soc_check3.checkLimit())
        self.assertFalse(charge_rate_check3.checkLimit())

        self.assertTrue(battery_is_ok(25, 70, 0.7))
        self.assertFalse(battery_is_ok(50, 85, 0))


if __name__ == '__main__':
    unittest.main()
