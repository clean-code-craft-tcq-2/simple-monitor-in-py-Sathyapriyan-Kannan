import BMSManagement as PermissibleLimit


class LimitChecker:
    def __init__(self, input_value, limit):
        self.input_value = input_value
        self.limit = limit

    def checkLimit(self):
        if self.input_value < self.limit.min_threshold or self.input_value > self.limit.max_threshold:
            self.print_log()
            return False

        return True

    def print_log(self):
        print(f'{self.limit.factor} is out of range!')


def battery_is_ok(temperature, soc, charge_rate):
    temp_check = LimitChecker(temperature, PermissibleLimit.temperature_limit)
    soc_check = LimitChecker(soc, PermissibleLimit.soc_limit)
    charge_rate_check = LimitChecker(charge_rate, PermissibleLimit.charge_rate_limit)

    return temp_check.checkLimit() and soc_check.checkLimit() and charge_rate_check.checkLimit()
