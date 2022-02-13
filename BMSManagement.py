class BMSManagement:
    def __init__(self, min_threshold, max_threshold, factor, issue_warning, warning_tolerance_rate=5):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.factor = factor
        self.issue_warning = issue_warning

        if issue_warning:

            warning_tolerance = self.max_threshold * (warning_tolerance_rate / 100)
            self.min_warn_tolerance = self.min_threshold + warning_tolerance
            self.max_warn_tolerance = self.max_threshold - warning_tolerance


temperature_limit = BMSManagement(0, 45, "Temperature", True)
soc_limit = BMSManagement(20, 80, "State of Charge", True)
charge_rate_limit = BMSManagement(0, 0.8, "Charge Rate", True)
