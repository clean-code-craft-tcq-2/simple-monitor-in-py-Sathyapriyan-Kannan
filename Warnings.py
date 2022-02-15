from BMSManagement import temperature_limit, soc_limit, charge_rate_limit


class WarningAlert:
    def __init__(self, warning_dict, limit_obj):
        self.__should_issue_warning = warning_dict['issue_warning']
        if warning_dict['issue_warning']:
            max_threshold = limit_obj.get_max_threshold()
            min_threshold = limit_obj.get_min_threshold()
            warning_tolerance = max_threshold * (warning_dict['warning_tolerance_rate'] / 100)
            self.__min_warn_tolerance = min_threshold + warning_tolerance
            self.__max_warn_tolerance = max_threshold - warning_tolerance
            self.__min_warn_alert_message = warning_dict['min_warning_msg']
            self.__max_warn_alert_message = warning_dict['max_warning_msg']

    def get_should_issue_warning(self):
        return self.__should_issue_warning

    def get_min_warn_tolerance(self):
        return self.__min_warn_tolerance

    def get_max_warn_tolerance(self):
        return self.__max_warn_tolerance

    def get_min_warn_alert_message(self):
        return self.__min_warn_alert_message

    def get_max_warn_alert_message(self):
        return self.__max_warn_alert_message


warn_temp = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                          'min_warning_msg': "Warning: Approaching lower Temperature",
                          'max_warning_msg': "Warning: Approaching peak Temperature"},
                         temperature_limit)

warn_soc = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                         'min_warning_msg': "Warning: Approaching discharge",
                         'max_warning_msg': "Warning: Approaching charge-peak"},
                        soc_limit)

warn_charge_rate = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                                 'min_warning_msg': "Warning: Approaching lower Charge Rate",
                                 'max_warning_msg': "Warning: Approaching peak Charge Rate"},
                                charge_rate_limit)
