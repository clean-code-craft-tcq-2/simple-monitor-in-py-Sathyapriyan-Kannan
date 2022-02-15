from BMSManagement import temperature_limit, soc_limit, charge_rate_limit,lang


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


temp_warning_message = {'EN': {'min_warning_msg': "Warning: Approaching lower Temperature",
                               'max_warning_msg': "Warning: Approaching peak Temperature"},
                        'DE': {'min_warning_msg': "Warnung: Annäherung an untere Temperatur",
                               'max_warning_msg': "Warnung vor nahender Spitzentemperatur"}
                        }
soc_warning_message = {'EN': {'min_warning_msg': "Warning: Approaching discharge",
                              'max_warning_msg': "Warning: Approaching charge-peak"},
                       'DE': {'min_warning_msg': "Warnung: vor nahender Entladung",
                              'max_warning_msg': "Warnung: Annäherung an Ladespitze"}
                       }
charge_rate_warning_message = {'EN': {'min_warning_msg': "Warning: Approaching lower Charge Rate",
                                      'max_warning_msg': "Warning: Approaching peak Charge Rate"},
                               'DE': {'min_warning_msg': "Warnung: Annäherung an die niedrigere Laderate",
                                      'max_warning_msg': "Warnung: Annäherung an Spitzenladungsrate"}
                               }

warn_temp = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                          'min_warning_msg': temp_warning_message[lang]['min_warning_msg'],
                          'max_warning_msg': temp_warning_message[lang]['max_warning_msg']},
                         temperature_limit)

warn_soc = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                         'min_warning_msg': soc_warning_message[lang]['min_warning_msg'],
                         'max_warning_msg': soc_warning_message[lang]['max_warning_msg']},
                        soc_limit)

warn_charge_rate = WarningAlert({'issue_warning': True, 'warning_tolerance_rate': 5,
                                 'min_warning_msg': charge_rate_warning_message[lang]['min_warning_msg'],
                                 'max_warning_msg': charge_rate_warning_message[lang]['max_warning_msg']},
                                charge_rate_limit)
