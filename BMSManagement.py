lang = 'DE'


class BMSManagement:
    def __init__(self, min_threshold, max_threshold, factor, alert_msg):
        self.__min_threshold = min_threshold
        self.__max_threshold = max_threshold
        self.__factor = factor
        self.__alert_msg = alert_msg

    def get_max_threshold(self):
        return self.__max_threshold

    def get_min_threshold(self):
        return self.__min_threshold

    def get_factor(self):
        return self.__factor

    def get_alert_msg(self):
        return self.__alert_msg


temp_warning_message = {'EN': {'factor': "Temperature",
                               'alert_msg': "is out of range!"},
                        'DE': {'factor': "Temperatur",
                               'alert_msg': "ist außer Reichweite!"}
                        }
soc_warning_message = {'EN': {'factor': "State of Charge",
                              'alert_msg': "is out of range!"},
                       'DE': {'factor': "Ladezustand",
                              'alert_msg': "ist außer Reichweite!"}
                       }
charge_rate_warning_message = {'EN': {'factor': "Charge Rate",
                                      'alert_msg': "is out of range!"},
                               'DE': {'factor': "Laderate",
                                      'alert_msg': "ist außer Reichweite!"}
                               }

temperature_limit = BMSManagement(0, 45, temp_warning_message[lang]['factor'], temp_warning_message[lang]['alert_msg'])
soc_limit = BMSManagement(20, 80, soc_warning_message[lang]['factor'], soc_warning_message[lang]['alert_msg'])
charge_rate_limit = BMSManagement(0, 0.8, charge_rate_warning_message[lang]['factor'], charge_rate_warning_message[lang]['alert_msg'])
