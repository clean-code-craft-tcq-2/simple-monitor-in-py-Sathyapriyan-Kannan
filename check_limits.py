import BMSManagement as PermissibleLimit
import Warnings as WarningAlert


class LimitChecker:
    def __init__(self, input_value, limit_obj, warn_obj):
        self.__input_value = input_value
        self.__limit = limit_obj
        self.__warn = warn_obj

    def get_input_value(self):
        return self.__input_value

    def check_if_not_in_min_threshold_limit(self):
        return self.__input_value < self.__limit.get_min_threshold()

    def check_if_not_in_max_threshold_limit(self):
        return self.__input_value > self.__limit.get_max_threshold()

    def check_is_in_limit(self):
        if self.check_if_not_in_min_threshold_limit() or self.check_if_not_in_max_threshold_limit():
            self.print_breach_alert()
            return False
        else:
            self.check_for_warnings()
            return True

    def check_for_warnings(self):
        if self.__warn.get_should_issue_warning():
            self.check_and_issue_warnings()
        pass

    def check_if_not_in_min_warning_limit(self):
        return self.__limit.get_min_threshold() <= self.__input_value <= self.__warn.get_min_warn_tolerance()

    def check_if_not_in_max_warning_limit(self):
        return self.__warn.get_max_warn_tolerance() <= self.__input_value <= self.__limit.get_max_threshold()

    def check_and_issue_warnings(self):
        if self.check_if_not_in_min_warning_limit():
            self.print_warning_alert(self.__warn.get_min_warn_alert_message())
            return True
        if self.check_if_not_in_max_warning_limit():
            self.print_warning_alert(self.__warn.get_max_warn_alert_message())
            return True
        return False

    def print_breach_alert(self):
        print(f'{self.__limit.get_factor()} {self.__limit.get_alert_msg()}')

    def print_warning_alert(self, warn_message):
        print(f'{warn_message}')


def battery_is_ok(temperature, soc, charge_rate):
    temp_check = LimitChecker(temperature, PermissibleLimit.temperature_limit, WarningAlert.warn_temp)
    soc_check = LimitChecker(soc, PermissibleLimit.soc_limit, WarningAlert.warn_soc)
    charge_rate_check = LimitChecker(charge_rate, PermissibleLimit.charge_rate_limit, WarningAlert.warn_charge_rate)

    isTemperatureInRange = temp_check.check_is_in_limit()
    isSocInRange = soc_check.check_is_in_limit()
    isChargeRateInRange = charge_rate_check.check_is_in_limit()

    return isTemperatureInRange and isSocInRange and isChargeRateInRange
