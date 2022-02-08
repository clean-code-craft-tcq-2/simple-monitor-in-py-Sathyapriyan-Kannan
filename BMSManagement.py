class BMSManagement:
    def __init__(self, min_threshold, max_threshold, factor):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.factor = factor


temperature_limit = BMSManagement(0, 45, "Temperature")
soc_limit = BMSManagement(20, 80, "State of Charge")
charge_rate_limit = BMSManagement(0, 0.8, "Charge Rate")
