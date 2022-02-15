import unittest
from check_limits import LimitChecker, battery_is_ok
import BMSManagement as PermissibleLimit
import Warnings as WarningAlert


class MyTestCase(unittest.TestCase):

    def test_limit_checker(self):
        temp_check = LimitChecker(25, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check = LimitChecker(70, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check = LimitChecker(0.7, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertEqual(25, temp_check.get_input_value())
        self.assertEqual(70, soc_check.get_input_value())
        self.assertEqual(0.7, charge_rate_check.get_input_value())

    def test_battery_is_ok(self):
        self.assertTrue(battery_is_ok(25, 23, 0.7))
        self.assertFalse(battery_is_ok(50, 77, 0))

    def test_check_in_limit(self):
        temp_check = LimitChecker(25, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check = LimitChecker(70, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check = LimitChecker(0.7, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertTrue(temp_check.check_in_limit())
        self.assertTrue(soc_check.check_in_limit())
        self.assertTrue(charge_rate_check.check_in_limit())

        # test above allowed limits
        temp_check2 = LimitChecker(46, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check2 = LimitChecker(81, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check2 = LimitChecker(0.9, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertEqual(46, temp_check2.get_input_value())
        self.assertEqual(81, soc_check2.get_input_value())
        self.assertEqual(0.9, charge_rate_check2.get_input_value())
        self.assertFalse(temp_check2.check_in_limit())
        self.assertFalse(soc_check2.check_in_limit())
        self.assertFalse(charge_rate_check2.check_in_limit())

        # test below allowed limits
        temp_check3 = LimitChecker(-1, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check3 = LimitChecker(19, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check3 = LimitChecker(-1, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertEqual(-1, temp_check3.get_input_value())
        self.assertEqual(19, soc_check3.get_input_value())
        self.assertEqual(-1, charge_rate_check3.get_input_value())
        self.assertFalse(temp_check3.check_in_limit())
        self.assertFalse(soc_check3.check_in_limit())
        self.assertFalse(charge_rate_check3.check_in_limit())

    def test_check_for_warning(self):
        temp_check = LimitChecker(2, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check = LimitChecker(25, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check = LimitChecker(1, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertTrue(temp_check.is_warning_issued())
        self.assertFalse(soc_check.is_warning_issued())
        self.assertFalse(charge_rate_check.is_warning_issued())

        # test above warning limits
        temp_check = LimitChecker(42.76, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check = LimitChecker(77, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check = LimitChecker(0.77, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertTrue(temp_check.is_warning_issued())
        self.assertTrue(soc_check.is_warning_issued())
        self.assertTrue(charge_rate_check.is_warning_issued())

        # test below warning limits
        temp_check = LimitChecker(2.24, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
        soc_check = LimitChecker(23, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
        charge_rate_check = LimitChecker(0.039, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)
        self.assertTrue(temp_check.is_warning_issued())
        self.assertTrue(soc_check.is_warning_issued())
        self.assertTrue(charge_rate_check.is_warning_issued())


if __name__ == '__main__':
    unittest.main()
