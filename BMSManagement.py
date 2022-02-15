class BMSManagement:
    def __init__(self, min_threshold, max_threshold, factor):
        self.__min_threshold = min_threshold
        self.__max_threshold = max_threshold
        self.__factor = factor

    def get_max_threshold(self):
        return self.__max_threshold

    def get_min_threshold(self):
        return self.__min_threshold

    def get_factor(self):
        return self.__factor


temperature_limit = BMSManagement(0, 45, "Temperature")
soc_limit = BMSManagement(20, 80, "State of Charge")
charge_rate_limit = BMSManagement(0, 0.8, "Charge Rate")
